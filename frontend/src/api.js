import axios from "axios";

const apiBaseUrl =
  import.meta.env.VITE_API_URL ||
  (import.meta.env.DEV ? "http://localhost:8000/api" : undefined);

if (!apiBaseUrl) {
  throw new Error(
    "VITE_API_URL must be set to the deployed backend API URL (including /api).",
  );
}

const api = axios.create({
  baseURL: apiBaseUrl,
  headers: { "Content-Type": "application/json" },
});

export const getDashboard = () => api.get("/dashboard");
export const getEmployees = (search = "") =>
  api.get("/employees/", { params: search ? { search } : {} });
export const addEmployee = (data) => api.post("/employees/", data);
export const deleteEmployee = (id) => api.delete(`/employees/${id}`);
export const getTasks = (filters = {}) => api.get("/tasks/", { params: filters });
export const addTask = (data) => api.post("/tasks/", data);
export const updateTaskStatus = (id, status) =>
  api.patch(`/tasks/${id}/status`, { status });
export const deleteTask = (id) => api.delete(`/tasks/${id}`);

export function getErrorMessage(error) {
  const detail = error?.response?.data?.detail;
  if (Array.isArray(detail)) return detail.map((item) => item.msg).join(", ");
  return detail || error.message || "Something went wrong. Please try again.";
}
