import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import { LayoutDashboard, Users, ClipboardList, BriefcaseBusiness } from "lucide-react";
import Dashboard from "./pages/Dashboard";
import Employees from "./pages/Employees";
import Tasks from "./pages/Tasks";

const navItems = [
  { to: "/", label: "Dashboard", icon: LayoutDashboard, end: true },
  { to: "/employees", label: "Employees", icon: Users },
  { to: "/tasks", label: "Tasks", icon: ClipboardList },
];

export default function App() {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark"><BriefcaseBusiness size={21} /></div>
          <div><strong>TaskFlow</strong><span>WORKSPACE</span></div>
        </div>
        <div className="nav-caption">WORKSPACE</div>
        <nav className="nav-list">
          {navItems.map(({ to, label, icon: Icon, end }) => (
            <NavLink key={to} to={to} end={end} className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Icon size={18} /><span>{label}</span>
            </NavLink>
          ))}
        </nav>
        <div className="sidebar-bottom">
          <div className="help-card">
            <div className="help-icon">?</div>
            <strong>Need a hand?</strong>
            <p>Manage your team's work in one place.</p>
          </div>
          <div className="profile-mini"><div className="avatar">A</div><div><strong>Admin User</strong><span>Workspace admin</span></div></div>
        </div>
      </aside>
      <main className="main-area">
        <header className="topbar">
          <div><span className="topbar-kicker">WORKSPACE / MANAGEMENT</span><h1>Employee Task Tracker</h1></div>
          <div className="topbar-right"><span className="online-dot" /> All systems operational</div>
        </header>
        <div className="page-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/employees" element={<Employees />} />
            <Route path="/tasks" element={<Tasks />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
        <footer className="footer">TaskFlow <span>•</span> Employee Task Tracker</footer>
      </main>
    </div>
  );
}
