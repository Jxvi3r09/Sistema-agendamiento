window.onload = function () {
    document.getElementById("welcomeModal").classList.remove("hidden");
};

function closeModal() {
    document.getElementById("welcomeModal").classList.add("hidden");
    document.getElementById("mainContent").classList.remove("hidden");
}