import axios from "axios";

// Base URL of your backend
// Use same-origin in production; allow override via env for local/dev
const isBrowser = typeof window !== "undefined";
const isDev = isBrowser && window.location.hostname === "localhost";
const BASE_URL =
  process.env.REACT_APP_API_BASE_URL ||
  (isDev ? "http://127.0.0.1:8000" : (isBrowser ? window.location.origin : "http://127.0.0.1:8000"));

export const processReport = async (reportText) => {
  try {
    const response = await axios.post(`${BASE_URL}/process-report`, {
      report: reportText,
    });
    return response.data;
  } catch (error) {
    console.error("Error processing report:", error);
    throw error;
  }
};

export const getReports = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/reports`);
    return response.data;
  } catch (error) {
    console.error("Error fetching reports:", error);
    throw error;
  }
};

export const translateOutcome = async (outcome, language) => {
  try {
    const response = await axios.post(`${BASE_URL}/translate`, {
      outcome: outcome,
      lang: language
    });
    return response.data;
  } catch (error) {
    console.error("Error translating outcome:", error);
    throw error;
  }
};