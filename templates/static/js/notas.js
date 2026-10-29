const modal = document.getElementById("novanota");
const buttonEditar = document.querySelectorAll(".editarCard");
const buttonCancelarEdit = document.querySelectorAll(".cancelarEditar");
let card;
let conteudoOriginal;
let tituloOriginal;

function abrirModal() {
  modal.showModal();
}

function fecharModal() {
  modal.close();
}

const textareas = document.querySelectorAll(".cardscontent");

textareas.forEach(regularAltura);

function regularAltura(textarea) {
  textarea.style.height = "auto";
  textarea.style.height = `${textarea.scrollHeight}px`;
}

textareas.forEach((textarea) => {
  textarea.addEventListener("input", ()=>{
    regularAltura(textarea)
  })
});

buttonEditar.forEach(editar);

function editar(button) {
  button.addEventListener("click", () => {
    card = button.closest("form");

    tituloOriginal = card.querySelector(".tituloCard").value;
    conteudoOriginal = card.querySelector(".cardscontent").value;
    card.querySelector(".tituloCard").removeAttribute("readonly");
    card.querySelector(".cardscontent").removeAttribute("readonly");

    card.querySelector(".menuCard").classList.toggle("hidden");
    card.querySelector(".editarMenu").classList.toggle("hidden");
  });
}

buttonCancelarEdit.forEach(cancelarEditar);

function cancelarEditar(cancelar) {
  cancelar.addEventListener("click", () => {
    card = cancelar.closest("form");
    card.querySelector(".menuCard").classList.toggle("hidden");
    card.querySelector(".editarMenu").classList.toggle("hidden");

    card.querySelector(".tituloCard").value = tituloOriginal;
    card.querySelector(".cardscontent").value = conteudoOriginal;

    card.querySelector(".tituloCard").setAttribute("readonly", "readonly");
    card.querySelector(".cardscontent").setAttribute("readonly", "readonly");

    regularAltura(card.querySelector(".cardscontent"))
  });
}

document.getElementById("notacontent").addEventListener("input", ()=>{
  regularAltura(document.getElementById("notacontent"))
})