import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const getTrucks = () => {
  return axios.get(`${API_URL}/trucks/`);
};

export const createTruck = (data) => {
  return axios.post(`${API_URL}/trucks/`, data);
};

export const updateTruck = (id, data) => {
  return axios.put(`${API_URL}/trucks/${id}/`, data);
};
