
import { useEffect, useRef } from 'react';
import L from "leaflet";

const MapComponent = () => {
    const mapElement = useRef(null)

    useEffect(() => {
        if (!mapElement.current) {
            return;
        }
        const map = L.map(mapElement.current).setView([51.505, -0.09], 13)
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map)
        return () => {
            map.remove();
        }
    }, []);

    return <div ref={mapElement} style={{height: "100vh", width:"100%"}}></div>
}
 
export default MapComponent;