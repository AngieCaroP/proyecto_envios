function toggleMenu() {
  const menu = document.getElementById('menu');
  menu.classList.toggle('show');
}
// Seleccionar todos los checkboxes
  const selectAll = document.getElementById('select-all');
  const checkboxes = document.querySelectorAll('.select-row');

    selectAll.addEventListener('change', () => {
      checkboxes.forEach(checkbox => {
        checkbox.checked = selectAll.checked;
      });
    });


  // Espera a que todo el DOM cargue
  document.addEventListener('DOMContentLoaded', () => {
    const hokoTitle = document.querySelector('.logo-title');
    const menu = document.querySelector('.menu');

    // Solo en móviles: alternar visibilidad al hacer clic en "HOKO"
    hokoTitle.addEventListener('click', () => {
      menu.classList.toggle('show');
    });
  });
