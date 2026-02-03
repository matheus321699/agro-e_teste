import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createTruck } from "../services/truckService";
import "../styles/form.css";
import "../styles/buttons.css";

const TruckForm = () => {
  const [form, setForm] = useState({
    license_plate: "",
    brand: "",
    model: "",
    manufacturing_year: "",
    fipe_price: ""
  });

  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();

    if (!form.license_plate || !form.brand || !form.model) {
      setError("Preencha todos os campos obrigatórios");
      return;
    }

    try {
      await createTruck(form);
      navigate("/");
    } catch (err) {
      setError(err.response?.data?.detail || "Erro ao salvar");
    }
  };

  return (
    <div className="container">
      <h1>Cadastrar Caminhão</h1>

      {error && <p className="error">{error}</p>}

      <form onSubmit={handleSubmit}>
        <input name="license_plate" placeholder="Placa" onChange={handleChange} />
        <input name="brand" placeholder="Marca" onChange={handleChange} />
        <input name="model" placeholder="Modelo" onChange={handleChange} />
        <input name="manufacturing_year" type="number" placeholder="Ano" onChange={handleChange} />
        <input name="fipe_price" type="number" placeholder="Preço FIPE" onChange={handleChange} />

        <div className="actions">
          <button type="submit" className="btn primary">Salvar</button>

          {/* 🔙 BOTÃO DE VOLTAR */}
          <button
            type="button"
            className="btn secondary"
            onClick={() => navigate("/")}
          >
            Voltar
          </button>
        </div>
      </form>
    </div>
  );
};

export default TruckForm;
