import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginForm from "@/components/login/LoginForm";
import Dashboard from "@/components/dashboard/Dashboard";
import DashboardLayout from "@/components/layouts/DashboardLayout";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginForm />} />
        <Route element={<DashboardLayout />}>
          <Route path="/" element={<Dashboard />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
