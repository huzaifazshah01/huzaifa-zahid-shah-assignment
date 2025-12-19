function SearchBar({value, onChange}) {
  return(
    <div className="search-box">
      <input type = "text" 
      placeholder="Search employees by name or department...."
      value = {value}
      onChange={(e) => onChange(e.target.value)}
      />
    </div>
  )
}

export default SearchBar;