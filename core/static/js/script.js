var car = [6, 7, 8];
console.log(car);
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

