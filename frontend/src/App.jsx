import { useEffect, useState } from "react";
import { searchEmployees } from "./services/employeeApi";
import SearchBar from "./components/SearchBar";
import EmployeeList from "./components/EmployeeList";


function App(){
  const [query, setQuery] = useState("");
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    if (!query) {
      setEmployees([]);
      return;
    }

  const timer = setTimeout(() => {
    searchEmployees(query)
    .then(data => setEmployees(data))
    .catch(error => console.error("Error fetching employees:", error));
  }, 400);
  return () => clearTimeout(timer);
  },[query]);

  return (
    <div style = {{padding: "2rem", fontFamily: "Arial"}}>
      <h1>Employee Directory Search System</h1>
      <SearchBar value={query} onChange={setQuery} />
      <EmployeeList employees={employees} />
      </div>
  );
}

export default App;
