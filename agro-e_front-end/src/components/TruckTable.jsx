const TruckTable = ({ trucks }) => {
  return (
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>Placa</th>
          <th>Marca</th>
          <th>Modelo</th>
          <th>Ano</th>
          <th>Preço FIPE</th>
        </tr>
      </thead>
      <tbody>
        {trucks.map((truck) => (
          <tr key={truck.id}>
            <td>{truck.license_plate}</td>
            <td>{truck.brand}</td>
            <td>{truck.model}</td>
            <td>{truck.manufacturing_year}</td>
            <td>R$ {truck.fipe_price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TruckTable;
