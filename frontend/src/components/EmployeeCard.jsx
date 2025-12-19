function EmployeeCard({ employee }) {
  return(
    <div className="employee-card">
      <div className = "employee-header">
      <h3>{employee.name}</h3>
      </div>
      <div className="employee-details">
      <p><strong>Email:</strong> {employee.email}</p>
      <p><strong>Department:</strong> {employee.department}</p>
      <p><strong>Date of Joining:</strong> {employee.date_of_joining ? new Date(employee.date_of_joining).toLocaleDateString() : "-"}</p>
      </div>

    </div>
  );
}

export default EmployeeCard;