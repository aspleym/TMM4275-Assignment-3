import { render, mazePreviewFromFile, mazePreviewFromURL } from "./preview.js";

var mLength = 100;
var mWidth = 100;
var mazeComplexity = 4;
var mazeName = null;
var fileList = [];

const lengthInput = document.getElementById("mLength");
const widthInput = document.getElementById("mWidth");

lengthInput.addEventListener("change", () => {
  mLength = lengthInput.value;
});

widthInput.addEventListener("change", () => {
  mWidth = widthInput.value;
  console.log(mWidth);
});

const fileInput = document.getElementById("import");
// Listen if user uploads file
fileInput.addEventListener("change", () => {
  fileList = fileInput.files;
  console.log(fileList[0]);
  mazePreviewFromFile(fileList[0], false);

  mazeName = null;
  changeMazeComplexity(4);
});

const lowButton = document.getElementById("low-btn");
// Listen if user selects a predefiend maze
lowButton.addEventListener("click", () => {
    mazeComplexity = 0;
  fileInput.value = null;
  changeMazeComplexity(0);
});

const mediumButton = document.getElementById("medium-btn");
// Listen if user selects a predefiend maze
mediumButton.addEventListener("click", () => {
  mazeComplexity = 1;
  fileInput.value = null;
  changeMazeComplexity(1);
});

const highButton = document.getElementById("high-btn");
// Listen if user selects a predefiend maze
highButton.addEventListener("click", () => {
  mazeComplexity = 2;
  fileInput.value = null;
  changeMazeComplexity(2);
});

const extremeButton = document.getElementById("extreme-btn");
// Listen if user selects a predefiend maze
extremeButton.addEventListener("click", () => {
  mazeComplexity = 3;
  fileInput.value = null;
  changeMazeComplexity(3);
});

const btnGroup = [lowButton, mediumButton, highButton, extremeButton];

// Move blue background and retrive name when user selects a predefined maze
function changeMazeComplexity(value) {
  for (var i in btnGroup) {
    if (i == parseInt(value)) {
      btnGroup[i].style.backgroundColor = "#008cff";
      btnGroup[i].style.color = "#fff";
      mazeName = "maze" + value + ".csv";
      if ([0,1,2,3].includes(parseInt(value))) {
          mazePreviewFromURL('./Maze/Uploaded/maze'+ value + '.csv', false);
      }
      console.log("changed to " + value);
    } else {
      btnGroup[i].style.backgroundColor = "#fff";
      btnGroup[i].style.color = "#008cff";
    }
  }
}
// Sets selected maze to "low" when page loads
window.onload = () => {
  render(document);
  changeMazeComplexity(0);
};
// Catch when user submits
window.onsubmit = (e) => {
  e.preventDefault();
  console.log("Submited");
  var request = new XMLHttpRequest();

  request.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("done");
      // Redirects to order
      if (mazeName !== null) {
        window.location.assign("Wall-E/order.html?" + mazeName.split(".")[0]);
      } else {
        window.location.assign(
          "Wall-E/order.html?" + fileList[0].name.split(".")[0]
        );
      }
    }
  };
  // Checks is user has selected a predefiend maze
  if (mazeName !== null) {
    console.log(mazeName);
    request.open("POST", "");
    request.setRequestHeader("content-type", "text/plain; charset=utf-8");
    request.setRequestHeader("Access-Control-Allow-Origin", "*");
    request.send(mazeName);
  } else if (mazeName === null && fileList !== []) {
    // OR if the user has uploaded a custom csv
    console.log("sending file");
    var formData = new FormData();
    formData.append("file", fileList[0]);
    request.open("POST", "");
    request.setRequestHeader("Access-Control-Allow-Origin", "*");
    request.send(formData);
  }
};
