document.addEventListener('DOMContentLoaded', (event) => {
    // Coordenadas del lugar específico
    const initialCoordinates = {
        lat: 13.6929403,
        lng: -89.2181911
    };

    // Inicialización del mapa
    const map = new maplibregl.Map({
        container: 'map', // container id
        style: 'https://demotiles.maplibre.org/style.json', // style URL
        center: [initialCoordinates.lng, initialCoordinates.lat], // starting position [lng, lat]
        zoom: 8 // starting zoom
    });

    // Añadir un marcador que se puede arrastrar
    let marker = new maplibregl.Marker({
        draggable: true
    })
    .setLngLat([initialCoordinates.lng, initialCoordinates.lat])
    .addTo(map);

    // Función para actualizar la posición del marcador
    function onDragEnd() {
        const lngLat = marker.getLngLat();
        document.getElementById('cent').value = `${lngLat.lat},${lngLat.lng}`;
    }

    // Event listeners
    marker.on('dragend', onDragEnd);
    map.on('click', (e) => {
        marker.setLngLat(e.lngLat);
        onDragEnd();
    });
});
