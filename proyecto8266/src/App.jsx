import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    
    fetch('http://192.168.4.1') 
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error al obtener datos:', error));
  }, []);

  return (
    <div className="App">
      <h1>Datos del ESP8266</h1>
      {data ? (
        <div>
          <p>Temperatura: {data.temperatura}°C</p>
          <p>Humedad: {data.humedad}%</p>
        </div>
      ) : (
        <p>Cargando datos...</p>
      )}
    </div>
  );
}

export default App;