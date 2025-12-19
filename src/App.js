import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import AdminLogin from "./components/AdminLogin";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/AdminLogin" element={<AdminLogin />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
