let arrayArea = document.getElementById("array");
let stepDuration = 50;
let pillarType = "height";
let pillarColor = "black";
let compColor = "green";
let swapColor = "red";

let currentAlgo = null;
let swapCount = 0;
let extraSpaceUsed = 0;
let arr = [];

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

function updatePillar(arr, i) {
  if (pillarType === "height") {
    arrayArea.children[i].style.backgroundColor = pillarColor;
    arrayArea.children[i].style.height = (arr[i] / arr.length * 90) + "%";
  } else if (pillarType === "grayscale") {
    arrayArea.children[i].style.height = "100%";
    let c = (arr[i] / arr.length * 255);
    arrayArea.children[i].style.backgroundColor = "rgb(" + c + ", " + c + ", " + c + ")";
  }
}

async function blinkPair(i, j, color, duration) {
  let iColor = arrayArea.children[i].style.backgroundColor;
  let jColor = arrayArea.children[j].style.backgroundColor;
  arrayArea.children[i].style.backgroundColor = color;
  arrayArea.children[j].style.backgroundColor = color;
  await sleep(duration);
  arrayArea.children[i].style.backgroundColor = iColor;
  arrayArea.children[j].style.backgroundColor = jColor;
}

function initialize(n) {
  arrayArea.innerHTML = "";
  let arr = Array.from({length: n}, (_, i) => i + 1);
  for (let i=0; i<n; i++) {
    let pillar = document.createElement("div");
    pillar.style.width = (100 / n) + "%";
    arrayArea.appendChild(pillar);
    updatePillar(arr, i);
  }
  return arr;
}

async function comp(arr, i, j) {
  await blinkPair(i, j, compColor, stepDuration);
  if (arr[i]  >  arr[j]) return "greater";
  if (arr[i]  <  arr[j]) return "less";
  if (arr[i] === arr[j]) return "equal";
}

async function swap(arr, i, j) {
  swapCount++;
  await blinkPair(i, j, swapColor, stepDuration);
  [arr[i], arr[j]] = [arr[j], arr[i]];
  updatePillar(arr, i);
  updatePillar(arr, j);
}

async function validate(arr) {
  let sorted = true;
  for (let i=0; i<arr.length-1; i++) {
    arrayArea.children[i].style.backgroundColor = compColor;
    if (arr[i] > arr[i+1]) {
      sorted = false;
      for (let j=0; j<i; j++)
        arrayArea.children[j].style.backgroundColor = swapColor;
      break;
    }
    await sleep(stepDuration);
  }
  await sleep(50);
  for (let i=0; i<arr.length; i++)
    updatePillar(arr, i);
  alert("The array is " + (sorted ? "sorted!" : "not sorted."));
}

async function shuffle(arr) {
  for (let i=0; i<arr.length; i++) {
    let j = Math.floor(Math.random() * arr.length);
    await swap(arr, i, j);
  }
}

let algorithms = {
  "Bubble Sort": async function(arr) {
    for (let i=0; i<arr.length; i++)
      for (let j=0; j<arr.length-i-1; j++)
        if (await comp(arr, j, j+1) == "greater")
          await swap(arr, j, j+1);
  },
  "Selection Sort": async function(arr) {
    for (let i = 0; i < arr.length; i++) {
      let minIdx = i;
      for (let j = i + 1; j < arr.length; j++) {
        if (await comp(arr, j, minIdx) === "less") {
          minIdx = j;
        }
      }
      if (minIdx !== i) await swap(arr, i, minIdx);
    }
  },
  "Insertion Sort": async function(arr) {
    for (let i = 1; i < arr.length; i++) {
      let j = i;
      while (j > 0 && await comp(arr, j, j - 1) === "less") {
        await swap(arr, j, j - 1);
        j--;
      }
    }
  },
  "Merge Sort": async function(arr) {
    async function mergeSort(arr, l, r) {
      if (l >= r) return;
      const m = Math.floor((l + r) / 2);
      await mergeSort(arr, l, m);
      await mergeSort(arr, m + 1, r);
      let n = r - l + 1;
      let p = l;
      let q = m + 1;
      let temp = [];
      for (let i=0; i<n; i++) {
        if (p > m || q <= r && await comp(arr, q, p) === "less")
          temp.push(arr[q++]);
        else temp.push(arr[p++]);
      }
      for (let i=l; i<=r; i++) {
        arr[i] = temp[i - l];
        await swap(arr, i, i);
      }
    }
    await mergeSort(arr, 0, arr.length - 1);
  },
  "Quick Sort": async function(arr) {
    async function partition(arr, l, r) {
      if (l >= r) return;
      let i = l - 1;
      for (let j=l; j<=r; j++)
        if (await comp(arr, j, r) == "less")
          await swap(arr, ++i, j);
      await swap(arr, ++i, r);
      await partition(arr, l, i-1);
      await partition(arr, i+1, r);
    }
    await partition(arr, 0, arr.length-1);
  }
};

window.onload = () => {
  arr = initialize(100);

  document.querySelectorAll(".nav-button").forEach(btn => {
    btn.addEventListener("click", () => {
      currentAlgo = btn.dataset.algo;
    });
  });

  document.getElementById("randomBtn").addEventListener("click", () => {
    const n = parseInt(document.getElementById("N").value);
    if (!n || n <= 0) {
      alert("Please enter a valid value for N.");
      return;
    }
    arr = initialize(n);
    shuffle(arr);
  });

  document.getElementById("startBtn").addEventListener("click", async () => {
    if (!currentAlgo || !algorithms[currentAlgo]) {
      alert("Please select an algorithm first.");
      return;
    }
    if (!arr.length) {
      alert("Please generate or enter an array first.");
      return;
    }
    swapCount = 0;
    await algorithms[currentAlgo](arr);
    await validate(arr);
    await runTests();
  });
};

async function updateExtraSpaceUsed(algorithmName, arr) {
  if (algorithmName === "Merge Sort") {
    extraSpaceUsed = arr.length;
  } else if (algorithmName === "Quick Sort") {
    extraSpaceUsed = Math.log2(arr.length);
  } else {
    extraSpaceUsed = 1;
  }
}

async function runTests() {
  const input = arr;
  const expected = [...input].sort((a, b) => a - b);

  console.log(`\n===== TEST REPORT =====`);
  console.log(`Algorithm: ${currentAlgo}`);
  console.log(`Input size: ${input.length}`);
  console.log(`Swap count: ${swapCount}`);

  await updateExtraSpaceUsed(currentAlgo, input);
  console.log(`Extra space used: ${extraSpaceUsed}`);

  const isSorted = input.every((val, i) => val === expected[i]);
  console.log(`Sorted correctly: ${isSorted}`);

  if (!isSorted) {
    console.error("Array is not sorted correctly!");
  }

  if (currentAlgo === "Bubble Sort" || currentAlgo === "Insertion Sort" || currentAlgo === "Selection Sort") {
    console.log(`Expected extra space: O(1)`);
  } else if (currentAlgo === "Merge Sort") {
    console.log(`Expected extra space: O(n)`);
  } else if (currentAlgo === "Quick Sort") {
    console.log(`Expected extra space: O(log n)`);
  }

  console.log(`========================\n`);
}