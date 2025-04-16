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


