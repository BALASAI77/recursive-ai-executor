import { useState } from 'react';

function TestUI() {
  const [prompt, setPrompt] = useState('');
  const [code, setCode] = useState('');

  const handleGenerate = () => {
    if (prompt.toLowerCase().includes('add two numbers')) {
      setCode('def add(a, b):\n return a + b');
    } else {
      setCode('# Your generated code will appear here...');
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 px-4">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Recursive AI Executor</h1>
      <p className="text-lg text-gray-700 mb-2">Enter your prompt:</p>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Write a function that adds two numbers"
        className="border border-gray-300 px-4 py-2 w-[700px] mb-4 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        rows={6}
        style={{ borderRadius: '1rem', fontSize: '1.25rem' }} // Larger placeholder font
      />
      <div>
        <button
          onClick={handleGenerate}
          className="bg-blue-600 text-white font-semibold rounded-md shadow-md hover:bg-blue-700 transition"
          style={{ marginTop: '18px', padding: '16px 40px', fontSize: '28px', width: '300px' }} // Custom size
        >
          Generate Code
        </button>
      </div>
      <pre className="mt-6 bg-gray-900 text-green-400 p-4 rounded-md text-left text-sm font-mono w-[400px] whitespace-pre-wrap shadow-lg">
        {code}
      </pre>
    </div>
  );
}

export default TestUI;