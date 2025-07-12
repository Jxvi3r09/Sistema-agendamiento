window.onload = function () {
  document.getElementById("welcomeModal").classList.remove("hidden");
};

function closeModal() {
  document.getElementById("welcomeModal").classList.add("hidden");
  document.getElementById("mainContent").classList.remove("hidden");
}

function mostrarPDF(input) {
  const file = input.files[0];
  const viewer = document.getElementById("pdfViewer");

  if (file && file.type === "application/pdf") {
    const fileURL = URL.createObjectURL(file);
    viewer.innerHTML = `<iframe src="${fileURL}" class="w-full h-full border rounded-lg"></iframe>`;
  } else {
    viewer.innerHTML = `<p class="text-red-500">Por favor seleccione un archivo PDF válido.</p>`;
  }
}
