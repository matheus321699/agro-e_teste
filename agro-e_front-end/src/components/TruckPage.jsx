import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getTrucks } from "../services/truckService";
import "../styles/table.css";
import "../styles/buttons.css";

const TruckPage = () => {
  const [trucks, setTrucks] = useState([]);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    loadTrucks();
  }, []);

  const loadTrucks = async () => {
    try {
      const response = await getTrucks();
      setTrucks(response.data);
    } catch {
      setError("Erro ao carregar caminhões");
    }
  };

  return (
    <div className="container">
      <h1>Caminhões</h1>

      {error && <p className="error">{error}</p>}

      <button className="btn primary" onClick={() => navigate("/trucks/new")}>
        + Novo Caminhão
      </button>

      <table>
        <thead>
          <tr>
            <th>Placa</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Ano</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {trucks.map(truck => (
            <tr key={truck.id}>
              <td>{truck.license_plate}</td>
              <td>{truck.brand}</td>
              <td>{truck.model}</td>
              <td>{truck.manufacturing_year}</td>
              <td>
                <button
                  className="btn secondary"
                  onClick={() => navigate(`/trucks/${truck.id}/edit`)}
                >
                  Editar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TruckPage;
