import React, { useState, useEffect } from "react";
import "./InferenceDisplay.css";

const InferenceDisplay = () => {
  const [inputPrompt, setInputPrompt] = useState("1");
  const [data, setData] = useState(null);
  const [layers, setLayers] = useState(null);
  const [loading, setLoading] = useState(false);
  const [clients, setClients] = useState([]);

  // Fetch layers and clients on mount
  useEffect(() => {
    fetchLayers();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch(
        `http://20.244.34.133:8084/?input_prompt=${inputPrompt}`
      );
      const result = await response.json();
      setData(result);
      setClients(result.connected_clients);
      fetchLayers(); // Refresh layers after inference
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    setLoading(false);
  };

  const fetchLayers = async () => {
    try {
      const response = await fetch("http://20.244.34.133:8084/display");
      const result = await response.json();
      setLayers(result.layers);
    } catch (error) {
      console.error("Error fetching layers:", error);
    }
  };

  const clearLayers = async () => {
    try {
      const response = await fetch("http://20.244.34.133:8084/clear", {
        method: "POST",
      });
      const result = await response.json();
      console.log(result.message);
      setLayers(null);
    } catch (error) {
      console.error("Error clearing layers:", error);
    }
  };

  return (
    <div className="container2">
      <h1>Inference Dashboard</h1>
      <div className="input-section">
        <input
          type="text"
          value={inputPrompt}
          onChange={(e) => setInputPrompt(e.target.value)}
          placeholder="Enter input prompt"
        />
        <button onClick={fetchData} disabled={loading}>
          {loading ? "Loading..." : "Run Inference"}
        </button>
      </div>
      
      {/* Connected Clients Section */}
      <div className="output-section">
        <h2>Connected Clients</h2>
        {clients.length > 0 ? (
          <ul>
            {clients.map((client) => (
              <li key={client}>{client}</li>
            ))}
          </ul>
        ) : (
          <p>No clients connected</p>
        )}
      </div>

      {/* Final Message Display */}
      {data && (
        <div className="output-section">
          <h2>Final Message</h2>
          <p className="final-message">{data.final_message}</p>
        </div>
      )}

      {/* Layer Details */}
      {layers && (
        <div className="layers-section">
          <h2>Layer Details</h2>
          {Object.entries(layers).map(([layer, clients]) => (
            <div key={layer} className="layer">
              <h3>Layer {layer}</h3>
              {clients.length > 0 ? (
                <ul>
                  {clients.map((client) => (
                    <li key={client.id}>{client.id} ({client.is_busy ? "Busy" : "Idle"})</li>
                  ))}
                </ul>
              ) : (
                <p>No clients in this layer</p>
              )}
            </div>
          ))}
          <button onClick={clearLayers} className="clear-button">
            Clear Layers
          </button>
        </div>
      )}
    </div>
  );
};

export default InferenceDisplay;
