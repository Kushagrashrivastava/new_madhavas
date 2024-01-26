var fchbtns = document.querySelectorAll(".fchmyBtn");
var fchbtns1 = document.querySelectorAll(".fchmyBtn1");
var fchbtns2 = document.querySelectorAll(".fchmyBtn3");
var fchmodals = document.querySelectorAll(".fchmodal");
var fchspans = document.querySelectorAll(".fchclose");

// Function to open the modal
function openModal(index) {
  fchmodals[index].style.display = "block";
}

// Function to close the modal
function closeModal(index) {
  fchmodals[index].style.display = "none";
}

// Event listeners for opening the modals
fchbtns.forEach(function (btn, index) {
  btn.addEventListener("click", function () {
    openModal(index);
  });
});
fchbtns1.forEach(function (btn, index) {
  btn.addEventListener("click", function () {
    openModal(index);
  });
});
fchbtns2.forEach(function (btn, index) {
  btn.addEventListener("click", function () {
    openModal(index);
  });
});

// Event listeners for closing the modals using the spans
fchspans.forEach(function (span, index) {
  span.addEventListener("click", function () {
    closeModal(index);
  });
});

// Event listeners for closing the modals when clicking outside the modals
window.addEventListener("click", function (event) {
  fchmodals.forEach(function (modal, index) {
    if (event.target == modal) {
      closeModal(index);
    }
  });
});
