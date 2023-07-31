const tabItems = document.querySelectorAll(".tab-item");
const tabContentItems = document.querySelectorAll(".tab-content-item");

function removeShowClass() {
  tabContentItems.forEach((item) => item.classList.remove("show"));
}

function removeBorder() {
  tabItems.forEach((item) => item.classList.remove("tab-border"));
}

function selectItem(e) {
  removeShowClass();
  removeBorder();
  this.classList.add("tab-border");
  const element = e.target;
  const something = element.id;
  const contentElement = "#" + something + "-content";
  document.querySelector(contentElement).classList.add("show");
}

tabItems.forEach((item) => item.addEventListener("click", selectItem));
