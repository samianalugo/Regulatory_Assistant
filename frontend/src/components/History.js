import React, { useEffect, useState } from "react";
import { getReports } from "../api";

const HistoryTable = () => {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const data = await getReports();
        setReports(data);
      } catch (error) {
        console.error("Failed to fetch reports:", error);
      }
    };
    fetchReports();
  }, []);

  if (reports.length === 0) return <p>No past reports found.</p>;

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>History of Processed Reports</h3>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr style={{ borderBottom: "2px solid #000" }}>
            <th style={{ padding: "10px", textAlign: "left" }}>Drug</th>
            <th style={{ padding: "10px", textAlign: "left" }}>Adverse Events</th>
            <th style={{ padding: "10px", textAlign: "left" }}>Severity</th>
            <th style={{ padding: "10px", textAlign: "left" }}>Outcome</th>
          </tr>
        </thead>
        <tbody>
          {reports.map((r) => (
            <tr key={r.id} style={{ borderBottom: "1px solid #ccc" }}>
              <td style={{ padding: "10px" }}>{r.drug}</td>
              <td style={{ padding: "10px" }}>{r.adverse_events.join(", ")}</td>
              <td style={{ padding: "10px" }}>{r.severity}</td>
              <td style={{ padding: "10px" }}>{r.outcome}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HistoryTable;
