const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

async function request(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  if (res.status === 204) return null;
  return res.json();
}

export const getRecipes = ({ page = 1, pageSize = 10, q = "" } = {}) => {
  const params = new URLSearchParams({ page, page_size: pageSize });
  if (q) params.set("q", q);
  return request(`/api/recipes/?${params.toString()}`);
};
export const getRecipe = (id) => request(`/api/recipes/${id}`);
export const createRecipe = (data) =>
  request("/api/recipes/", { method: "POST", body: JSON.stringify(data) });
export const updateRecipe = (id, data) =>
  request(`/api/recipes/${id}`, { method: "PUT", body: JSON.stringify(data) });
export const deleteRecipe = (id) =>
  request(`/api/recipes/${id}`, { method: "DELETE" });
