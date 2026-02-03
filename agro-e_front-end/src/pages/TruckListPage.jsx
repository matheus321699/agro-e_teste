import { useNavigate } from "react-router-dom";
import { useTrucks } from "../hooks/useTrucks";
import TruckTable from "../components/TruckTable";
import ErrorAlert from "../components/ErrorAlert";

const TruckListPage = () => {
  const { trucks, error, loading } = useTrucks();
  const navigate = useNavigate();

  return (
    <div>
      <h1>Caminhões</h1>

      <button onClick={() => navigate("/novo")}>
        Novo Caminhão
      </button>

      {error && <ErrorAlert message={error} />}
      {loading ? <p>Carregando...</p> : <TruckTable trucks={trucks} />}
    </div>
  );
};

export default TruckListPage;
