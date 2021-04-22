var mLength = 50;
var mWidth = 50;
var mHeight = 50;
var eMail = "";
var mazeComplexity = 4;
var mazeName = null;
var fileList = [];

const lengthInput = document.getElementById("mLength");
const widthInput = document.getElementById("mWidth");
const heightInput = document.getElementById("mHeight");
const emailInput = document.getElementById("emailInput");
const loader = document.getElementById("loader")

lengthInput.addEventListener("change", () => {
  mLength = lengthInput.value;
});

widthInput.addEventListener("change", () => {
  mWidth = widthInput.value;
});

heightInput.addEventListener("change", () => {
  mHeight = heightInput.value;
});

emailInput.addEventListener("change", () => {
  eMail = emailInput.value;
});

const fileInput = document.getElementById("import");
// Listen if user uploads file
fileInput.addEventListener("change", () => {
  fileList = fileInput.files;
  console.log(fileList[0]);
});

// window.onload = () => {};
// Catch when user submits

window.onsubmit = (e) => {
  e.preventDefault();
  console.log("Submited");

  loader.style.display = "block"
  var request = new XMLHttpRequest();
  var request2 = new XMLHttpRequest();

  request.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("done");
      if (fileList !== []) {
        // OR if the user has uploaded a custom csv
        console.log("sending info");
        var info =
          "NAME: " +
          fileList[0].name +
          "\n" +
          "EMAIL: " +
          eMail +
          "\n" +
          "LENGTH: " +
          mLength +
          "\n" +
          "WIDTH: " +
          mWidth +
          "\n" +
          "HEIGHT: " +
          mHeight;
        request2.open("POST", "");
        request2.setRequestHeader("content-type", "text/plain; charset=utf-8");
        request2.setRequestHeader("Access-Control-Allow-Origin", "*");
        request2.send(info);
      }
      /* Redirects to order
      if (false) {
        window.location.assign("WC/order.html?" + mazeName.split(".")[0]);
      } else {
        window.location.assign(
          "WC/order.html?" + fileList[0].name.split(".")[0]
        );
      }
      */
    }
  };

  request2.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("done with req2");
      // Redirects to order
      window.location.assign("WC/order.html?" + fileList[0].name.split(".")[0]);
    }
  };

  if (fileList !== []) {
    // OR if the user has uploaded a custom csv
    console.log("sending file");
    var formData = new FormData();
    formData.append("file", fileList[0]);
    request.open("POST", "");
    request.setRequestHeader("Access-Control-Allow-Origin", "*");
    request.send(formData);
  }
};
