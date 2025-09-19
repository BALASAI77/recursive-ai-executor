import React, { useState } from "react";

const BACKEND_URL = "https://recursive-ai-executor.onrender.com";

function App() {
  const [prompt, setPrompt] = useState("");
  const [generatedCode, setGeneratedCode] = useState("");
  const [terminalOutput, setTerminalOutput] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [retryCount, setRetryCount] = useState(0);

  const handleSubmit = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    setError("");
    setGeneratedCode("");
    setTerminalOutput("");
    setRetryCount(0);

    let success = false;
    let attempts = 0;

    while (!success && attempts < 3) {
      try {
        const response = await fetch(`${BACKEND_URL}/execute`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt }),
        });

        if (!response.ok) {
          throw new Error(`Backend error: ${response.status}`);
        }

        const data = await response.json();
        setGeneratedCode(data.final_code || "");
        setTerminalOutput(
          data.success
            ? data.output || "No output"
            : data.error || "Unknown error"
        );
        success = true;
      } catch (err) {
        attempts++;
        setRetryCount(attempts);
        if (attempts >= 3) {
          setError("# Error connecting to backend after max retries...");
        }
      }
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="w-full max-w-3xl bg-white shadow-lg rounded-2xl p-8">
        <h1 className="text-3xl font-bold text-center mb-6 text-indigo-600">
          Recursive AI Executor
        </h1>

        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt..."
          className="w-full border border-gray-300 rounded-lg p-4 mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          rows={4}
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="w-full bg-indigo-600 text-white font-semibold py-3 rounded-lg hover:bg-indigo-700 transition disabled:opacity-50"
        >
          {loading ? "Generating..." : "Generate Code"}
        </button>

        {error && (
          <div className="mt-4 text-red-600 font-semibold whitespace-pre-line">
            {error}
            {retryCount > 0 && (
              <p className="text-sm text-gray-500">
                Retry Attempts: {retryCount}
              </p>
            )}
          </div>
        )}

        {generatedCode && (
          <div className="mt-6">
            <h2 className="text-xl font-semibold mb-2 text-gray-700">
              Generated Code (Read-Only)
            </h2>
            <pre className="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto">
              {generatedCode}
            </pre>
          </div>
        )}

        {terminalOutput && (
          <div className="mt-6">
            <h2 className="text-xl font-semibold mb-2 text-gray-700">
              Terminal Output
            </h2>
            <pre className="bg-gray-900 text-yellow-300 p-4 rounded-lg overflow-x-auto">
              {terminalOutput}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
