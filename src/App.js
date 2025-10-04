// src/App.js
import React, { useState } from "react";
import ReportForm from "./components/ReportForm";
import ReportTable from "./components/ReportTable";
import HistoryTable from "./components/History";
import SeverityChart from "./components/SeverityChart";

function App() {
  const [result, setResult] = useState(null); // Stores the latest processed report

  return (
    <div style={{ maxWidth: "900px", margin: "0 auto", padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ textAlign: "center", marginBottom: "30px" }}>
        Mini Regulatory Report Assistant
      </h1>

      {/* Input form to paste a medical report */}
      <ReportForm setResult={setResult} />

      {/* Display the processed report in a table */}
      <ReportTable data={result} />

      {/* Display history of all processed reports */}
      <HistoryTable />

      {/* Display severity distribution chart */}
      <SeverityChart />
    </div>
  );
}

export default App;
