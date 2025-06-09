import { useEffect, useState } from "react";
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Dot
} from "recharts";

function CustomDot(props) {
  const { cx, cy, payload } = props;
  // Highlight dots only for "Recorded" status
  if (payload.status === "Recorded") {
    return (
      <circle cx={cx} cy={cy} r={6} fill="#FF4C4C" stroke="white" strokeWidth={2} />
    );
  }
  // For other points (Live), no visible dot or smaller dot
  return (
    <circle cx={cx} cy={cy} r={3} fill="#00C49F" />
  );
}

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/data")
      .then(res => res.json())
      .then(json => setData(json));
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h2 style={{ textAlign: "center", marginBottom: "2rem" }}>
        📊 Weight Trend Over Time
      </h2>
      <ResponsiveContainer width="100%" height={450}>
        <LineChart
          data={data}
          margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" tick={{ fontSize: 12 }} />
          <YAxis domain={["auto", "auto"]} tick={{ fontSize: 12 }} />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="weight"
            stroke="#00C49F"
            strokeWidth={3}
            dot={<CustomDot />}
            activeDot={{ r: 8 }}
            animationDuration={800}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;
