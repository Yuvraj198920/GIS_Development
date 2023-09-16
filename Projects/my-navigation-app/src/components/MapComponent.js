import { MapContainer, TileLayer } from "react-leaflet";

const MapComponent = () => {
    return (
        <MapContainer center={[51.505, -0.09]} zoom={13}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></TileLayer>
        </MapContainer>
    )
}

export default MapComponent;