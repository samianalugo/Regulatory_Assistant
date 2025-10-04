import React, { useState } from "react";
import { translateOutcome } from "../api";

const TranslationButton = ({ outcome }) => {
  const [translatedText, setTranslatedText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleTranslate = async (language) => {
    setLoading(true);
    setError("");
    
    try {
      const result = await translateOutcome(outcome, language);
      setTranslatedText(result.translated);
    } catch (err) {
      setError("Translation failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: "10px" }}>
      <div style={{ marginBottom: "10px" }}>
        <button
          onClick={() => handleTranslate("fr")}
          disabled={loading}
          style={{
            marginRight: "10px",
            padding: "5px 10px",
            backgroundColor: loading ? "#ccc" : "#28a745",
            color: "white",
            border: "none",
            borderRadius: "3px",
            cursor: loading ? "not-allowed" : "pointer",
            fontSize: "12px"
          }}
        >
          {loading ? "Translating..." : "🇫🇷 French"}
        </button>
        
        <button
          onClick={() => handleTranslate("sw")}
          disabled={loading}
          style={{
            padding: "5px 10px",
            backgroundColor: loading ? "#ccc" : "#ffc107",
            color: "black",
            border: "none",
            borderRadius: "3px",
            cursor: loading ? "not-allowed" : "pointer",
            fontSize: "12px"
          }}
        >
          {loading ? "Translating..." : "🇹🇿 Swahili"}
        </button>
      </div>
      
      {translatedText && (
        <div style={{
          padding: "8px",
          backgroundColor: "#f8f9fa",
          border: "1px solid #dee2e6",
          borderRadius: "4px",
          fontSize: "14px"
        }}>
          <strong>Translated:</strong> {translatedText}
        </div>
      )}
      
      {error && (
        <div style={{ color: "red", fontSize: "12px", marginTop: "5px" }}>
          {error}
        </div>
      )}
    </div>
  );
};

export default TranslationButton;
