const productos = {
  fit_short_m: {
    nombre: "Fit Short M",
    dropshipping: 18200,
    precio: 59200
  },
  camiseta_l: {
    nombre: "Camiseta L",
    dropshipping: 20000,
    precio: 65000
  }
};

function generarNumeroGuia() {
  // Simple ejemplo: genera un número aleatorio con prefijo
  const prefijo = "GUI-";
  const numeroAleatorio = Math.floor(Math.random() * 1000000);
  return prefijo + numeroAleatorio.toString().padStart(6, '0');
}

function colocarNumeroGuia() {
  const idEnvioSpan = document.getElementById('envio-id');
  if (idEnvioSpan) {
    idEnvioSpan.textContent = generarNumeroGuia();
  }
}

// Llama a la función para generar y colocar el número de guía al cargar la página
document.addEventListener('DOMContentLoaded', colocarNumeroGuia);

// (Opcional) Puedes llamarla en otro evento si lo deseas, por ejemplo,
// al enfocar el campo de ID (si lo tuvieras como input)
// const idEnvioInput = document.getElementById('envio-id');
// if (idEnvioInput) {
//   idEnvioInput.addEventListener('focus', colocarNumeroGuia);
// }

function sincronizarDatosFormulario() {
  const nombreInput = document.querySelector('input[name="nombre"]');
  const cantidadPaquetesSpan = document.getElementById('envio-cantidad-paquetes');
  const cantidadProductosSpan = document.getElementById('envio-cantidad-productos');
  const cobroTotalSpan = document.getElementById('envio-cobro-total');
  const precioManualInput = document.querySelector('input[name="precio_manual"]');
  const contenidoInput = document.querySelector('input[name="contenido"]');
  const cantidadProductoInput = document.querySelector('input[name="cantidad_producto_input"]');

  if (nombreInput && document.getElementById('envio-creado-por')) {
    document.getElementById('envio-creado-por').textContent = nombreInput.value;
  }

  if (cantidadProductoInput && cantidadPaquetesSpan) {
    cantidadPaquetesSpan.textContent = cantidadProductoInput.value;
  }

  if (contenidoInput && cantidadProductosSpan) {
    cantidadProductosSpan.textContent = contenidoInput.value;
  }

  if (precioManualInput && cobroTotalSpan) {
    cobroTotalSpan.textContent = precioManualInput.value + " COP";
  }
}

// Agrega event listeners a los campos del formulario para sincronizar los datos
document.addEventListener('DOMContentLoaded', () => {
  const nombreInput = document.querySelector('input[name="nombre"]');
  const precioManualInput = document.querySelector('input[name="precio_manual"]');
  const contenidoInput = document.querySelector('input[name="contenido"]');
  const cantidadProductoInput = document.querySelector('input[name="cantidad_producto_input"]');

  if (nombreInput) {
    nombreInput.addEventListener('input', sincronizarDatosFormulario);
  }
  if (precioManualInput) {
    precioManualInput.addEventListener('input', sincronizarDatosFormulario);
  }
  if (contenidoInput) {
    contenidoInput.addEventListener('input', sincronizarDatosFormulario);
  }
  if (cantidadProductoInput) {
    cantidadProductoInput.addEventListener('input', sincronizarDatosFormulario);
  }
});