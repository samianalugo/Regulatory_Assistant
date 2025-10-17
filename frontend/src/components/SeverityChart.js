import React, { useEffect, useState } from "react";
import { getReports } from "../api";

const SeverityChart = () => {
  const [severityData, setSeverityData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const reports = await getReports();
        const severityCounts = {};
        
        reports.forEach(report => {
          const severity = report.severity || 'unknown';
          severityCounts[severity] = (severityCounts[severity] || 0) + 1;
        });
        
        setSeverityData(severityCounts);
      } catch (error) {
        console.error("Failed to fetch severity data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading chart...</div>;

  const total = Object.values(severityData).reduce((sum, count) => sum + count, 0);
  if (total === 0) return <div>No data available for chart</div>;

  const getBarWidth = (count) => {
    return `${(count / total) * 100}%`;
  };

  const getBarColor = (severity) => {
    switch (severity.toLowerCase()) {
      case 'severe': return '#dc3545';
      case 'moderate': return '#ffc107';
      case 'mild': return '#28a745';
      default: return '#6c757d';
    }
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>Severity Distribution</h3>
      <div style={{ 
        border: "1px solid #ddd", 
        padding: "20px", 
        borderRadius: "8px",
        backgroundColor: "#f8f9fa"
      }}>
        {Object.entries(severityData).map(([severity, count]) => (
          <div key={severity} style={{ marginBottom: "15px" }}>
            <div style={{ 
              display: "flex", 
              justifyContent: "space-between", 
              marginBottom: "5px" 
            }}>
              <span style={{ 
                textTransform: "capitalize", 
                fontWeight: "bold",
                color: getBarColor(severity)
              }}>
                {severity}
              </span>
              <span>{count} ({Math.round((count / total) * 100)}%)</span>
            </div>
            <div style={{
              width: "100%",
              height: "20px",
              backgroundColor: "#e9ecef",
              borderRadius: "10px",
              overflow: "hidden"
            }}>
              <div style={{
                width: getBarWidth(count),
                height: "100%",
                backgroundColor: getBarColor(severity),
                transition: "width 0.3s ease"
              }} />
            </div>
          </div>
        ))}
        <div style={{ 
          marginTop: "15px", 
          fontSize: "14px", 
          color: "#6c757d",
          textAlign: "center"
        }}>
          Total Reports: {total}
        </div>
      </div>
    </div>
  );
};

export default SeverityChart;
