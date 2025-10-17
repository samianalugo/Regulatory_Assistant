import React, { useState } from "react";
import { processReport } from "../api";

const ReportForm = ({ setResult }) => {
  const [reportText, setReportText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!reportText.trim()) {
      setError("Please enter a report text");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const result = await processReport(reportText);
      setResult(result);
    } catch (err) {
      setError("Failed to process report. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setReportText(event.target.result);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div style={{ marginBottom: "30px" }}>
      <h3>Enter Medical Report</h3>
      
      {/* File Upload Option */}
      <div style={{ marginBottom: "15px" }}>
        <label style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>
          Or upload a file:
        </label>
        <input
          type="file"
          accept=".txt,.md"
          onChange={handleFileUpload}
          style={{ padding: "5px" }}
        />
      </div>

      {/* Text Input */}
      <form onSubmit={handleSubmit}>
        <textarea
          value={reportText}
          onChange={(e) => setReportText(e.target.value)}
          placeholder="Paste your medical report here... (e.g., Patient experienced severe nausea and headache after taking Drug X. Patient recovered.)"
          style={{
            width: "100%",
            height: "120px",
            padding: "10px",
            border: "1px solid #ccc",
            borderRadius: "4px",
            fontSize: "14px",
            resize: "vertical"
          }}
        />
        
        {error && (
          <div style={{ color: "red", marginTop: "10px" }}>
            {error}
          </div>
        )}

        <button
          type="submit"
          disabled={loading}
          style={{
            marginTop: "10px",
            padding: "10px 20px",
            backgroundColor: loading ? "#ccc" : "#007bff",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: loading ? "not-allowed" : "pointer",
            fontSize: "16px"
          }}
        >
          {loading ? "Processing..." : "Process Report"}
        </button>
      </form>
    </div>
  );
};

export default ReportForm;
