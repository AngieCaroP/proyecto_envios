document.getElementById('form-guia').addEventListener('submit', function (e) {
    e.preventDefault();
  
    // Capturar los datos del formulario
    const guia = {
      id: Math.floor(Math.random() * 100000),
      nombre: document.getElementById('nombre').value,
      telefono: document.getElementById('telefono').value,
      ciudad: document.getElementById('ciudad').value,
      direccion: document.getElementById('direccion').value,
      direccion_secundaria: document.getElementById('direccion_secundaria').value,
      tipo_id: document.getElementById('tipo_id').value,
      numero_id: document.getElementById('numero_id').value,
      correo: document.getElementById('correo').value,
      producto: document.getElementById('producto').value,
      medidas: {
        ancho: document.getElementById('ancho').value,
        alto: document.getElementById('alto').value,
        largo: document.getElementById('largo').value,
        peso: document.getElementById('peso').value,
      },
      valor_asegurado: document.getElementById('valor_asegurado').value,
      contenido: document.getElementById('contenido').value,
      forma_pago: document.getElementById('pago').value,
      estado: "Despachada",
      transportadora: "DOMINA RECAUDO",
      bodega: "FULFILLMENT BARRANQUILLA Tempus company",
      creado_por: "Juan Carlos San",
      paquetes: 2,
      productos: 0,
      total: 260009
    };
  
    // Guardar en localStorage simulando base de datos
    let guias = JSON.parse(localStorage.getItem("guias")) || [];
    guias.push(guia);
    localStorage.setItem("guias", JSON.stringify(guias));
  
    // Redirigir a la página de detalle
    window.location.href = `detalle_guia.html?id=${guia.id}`;
  });
  