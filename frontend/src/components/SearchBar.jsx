import React, { useState } from "react";

function SearchBar() {
  const [query, setQuery] = useState("");

  const handleSearch = () => {
    fetch(`/search?query=${query}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data); // Handle search results
      });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search organizations..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
}

export default SearchBar;
