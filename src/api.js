import axios from "axios";

// Base URL of your backend
const BASE_URL = "http://127.0.0.1:8000";

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