import React from "react";
import TranslationButton from "./TranslationButton";

const ReportTable = ({ data }) => {
    if (!data) return null;

    return(
        <div style={{ marginTop: "20px" }}>
      <h3>Processed Report</h3>
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
          <tr style={{ borderBottom: "1px solid #ccc" }}>
            <td style={{ padding: "10px" }}>{data.drug}</td>
            <td style={{ padding: "10px" }}>{data.adverse_events.join(", ")}</td>
            <td style={{ padding: "10px" }}>{data.severity}</td>
            <td style={{ padding: "10px" }}>
              {data.outcome}
              <TranslationButton outcome={data.outcome} />
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    );
};

export default ReportTable;