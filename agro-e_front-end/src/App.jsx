import { BrowserRouter, Routes, Route } from "react-router-dom";
import TruckPage from "./components/TruckPage";
import TruckForm from "./components/TruckForm";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<TruckPage />} />
        <Route path="/trucks/new" element={<TruckForm />} />
        <Route path="/trucks/:id/edit" element={<TruckForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
