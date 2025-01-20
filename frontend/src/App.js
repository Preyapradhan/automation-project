import React from "react";
import SearchBar from "./components/SearchBar";
import OrganizationList from "./components/OrganizationList";

function App() {
  return (
    <div>
      <h1>Crunchbase Organization Insights</h1>
      <SearchBar />
      <OrganizationList />
    </div>
  );
}

export default App;
