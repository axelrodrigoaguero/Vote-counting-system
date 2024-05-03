function mostrarInput(checkbox) {
  var card = checkbox.closest('.card');
  var headerCheckboxes = document.querySelectorAll('.header-checkbox');
  var bodyCheckboxes = card.querySelectorAll('.body-checkbox');
  var input = card.querySelector('.input-numerico');
  var textoAyuda = card.querySelector('.texto-ayuda');

  if (checkbox.checked) {
      input.style.display = 'block';
      textoAyuda.style.display = 'block';
      headerCheckboxes.forEach(function (headerCheckbox) {
          if (headerCheckbox !== checkbox) {
              headerCheckbox.disabled = true;
          }
      });
      bodyCheckboxes.forEach(function (checkbox) {
          checkbox.checked = true;
          checkbox.disabled = true;
      });
  } else {
      input.style.display = 'none';
      textoAyuda.style.display = 'none';
      headerCheckboxes.forEach(function (headerCheckbox) {
          if (headerCheckbox !== checkbox) {
              headerCheckbox.disabled = false;
          }
      });
      bodyCheckboxes.forEach(function (checkbox) {
          checkbox.checked = false;
          checkbox.disabled = true;
      });
  }
}

function reiniciarCheckboxes() {
  var headerCheckboxes = document.querySelectorAll('.header-checkbox');
  var bodyCheckboxes = document.querySelectorAll('.body-checkbox');
  var inputNumericos = document.querySelectorAll('.input-numerico');
  var textoAyudas = document.querySelectorAll('.texto-ayuda');

  headerCheckboxes.forEach(function (checkbox) {
      checkbox.checked = false;
      checkbox.disabled = false;
      mostrarInput(checkbox);
  });

  bodyCheckboxes.forEach(function (checkbox) {
      checkbox.checked = false;
      checkbox.disabled = true;
  });

  inputNumericos.forEach(function (input) {
      input.value = '';
  });

  textoAyudas.forEach(function (textoAyuda) {
      textoAyuda.style.display = 'none';
  });
}

const btn = document.getElementById('btn');
const botones = document.getElementById('botones');

btn.addEventListener('click', () => {
  botones.classList.toggle('mostrar');
});
