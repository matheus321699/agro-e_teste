import { useEffect, useState } from "react";
import { truckService } from "../services/truckService";

export function useTrucks() {
  const [trucks, setTrucks] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const loadTrucks = async () => {
    try {
      setLoading(true);
      const response = await truckService.getAll();
      setTrucks(response.data);
    } catch (err) {
      setError("Erro ao carregar caminhões");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTrucks();
  }, []);

  return { trucks, error, loading, loadTrucks };
}
