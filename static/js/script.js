const opi = document.querySelectorAll(".opi");
opi.forEach((i) => {
  if (i.textContent > 70) {
    i.classList.add("opi-green");
    console.log(i.textContent);
  }
  if (i.textContent < 70) {
    i.classList.add("opi-red");
    console.log(i.textContent);
  }
});

const dmenu = document.querySelector(".dropdown-menus");
const menuLink = document.querySelector(".dropdown-toggle");

menuLink.addEventListener("click", () => {
  console.log('clicked')
  dmenu.classList.toggle("show");
});

const equipment = document.getElementById("id_equipment");
const bConveyor = document.getElementById("div_id_bottle_conveyor");
bConveyor.style.display = "none";

equipment.addEventListener("change", (i) => {
  if (i.target.value == 9) {
    bConveyor.style.display = "block";
  } else {
    bConveyor.style.display = "none";
  }
});
