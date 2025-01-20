import React, { useState, useEffect } from "react";

function OrganizationList() {
  const [organizations, setOrganizations] = useState([]);

  useEffect(() => {
    fetch("/organizations")
      .then((response) => response.json())
      .then((data) => setOrganizations(data));
  }, []);

  return (
    <div>
      <h2>Organizations</h2>
      <ul>
        {organizations.map((org, index) => (
          <li key={index}>
            <h3>{org.name}</h3>
            <p>{org.location}</p>
            <p>{org.enrichment}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default OrganizationList;
