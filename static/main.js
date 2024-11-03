// const hamburger = document.querySelector(".hamburger");
// const navMenu = document.querySelector(".nav-menu");

// hamburger.addEventListener("click", mobileMenu);

// function mobileMenu() {
//   hamburger.classList.toggle("active");
//   navMenu.classList.toggle("active");
// }

// // when we click on hamburger icon its close

// const navLink = document.querySelectorAll(".nav-link");

// navLink.forEach((n) => n.addEventListener("click", closeMenu));

// function closeMenu() {
//   hamburger.classList.remove("active");
//   navMenu.classList.remove("active");
// }

// /*=============== SHOW MODAL ===============*/
// const showModal = (openButton, modalContent) => {
//   const openBtn = document.getElementById(openButton),
//     modalContainer = document.getElementById(modalContent);

//   if (openBtn && modalContainer) {
//     openBtn.addEventListener("click", () => {
//       modalContainer.classList.add("show-modal");
//     });
//   }
// };
// showModal("open-modal", "modal-container");

// /*=============== CLOSE MODAL ===============*/
// const closeBtn = document.querySelectorAll(".close-modal");

// function closeModal() {
//   const modalContainer = document.getElementById("modal-container");
//   modalContainer.classList.remove("show-modal");
// }
// closeBtn.forEach((c) => c.addEventListener("click", closeModal));
