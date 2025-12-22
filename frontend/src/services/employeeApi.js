const BASE_URL = import.meta.env.VITE_API_BASE_URL

export async function searchEmployees(search) {
  // const response = await fetch(`${BASE_URL}/employees?search=${encodeURIComponent(search)}`);
  const response = await fetch(`${BASE_URL}/employees?search=${query}`);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return await response.json();
}
