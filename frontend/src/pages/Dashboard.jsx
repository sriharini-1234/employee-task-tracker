import { useEffect, useState } from "react";
import { Users, ClipboardList, CheckCircle2, Clock3, ArrowUpRight } from "lucide-react";
import { Link } from "react-router-dom";
import { getDashboard, getTasks, getErrorMessage } from "../api";
import StatCard from "../components/StatCard";
import StatusBadge from "../components/StatusBadge";

export default function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([getDashboard(), getTasks()])
      .then(([dashboardResponse, taskResponse]) => {
        setSummary(dashboardResponse.data);
        setTasks(taskResponse.data.slice(0, 5));
      })
      .catch((err) => setError(getErrorMessage(err)));
  }, []);

  return (
    <>
      <div className="page-heading">
        <div><p className="eyebrow">OVERVIEW</p><h2>Dashboard</h2><p className="muted">Here's what's happening with your team today.</p></div>
        <Link className="primary-button" to="/tasks"> <span>＋</span> Create task</Link>
      </div>
      {error && <div className="alert error">{error} — Check that the API and database are running.</div>}
      <div className="stats-grid">
        <StatCard title="Total employees" value={summary?.total_employees} note="People in your workspace" icon={Users} tone="blue" />
        <StatCard title="Total tasks" value={summary?.total_tasks} note="Tasks created so far" icon={ClipboardList} tone="violet" />
        <StatCard title="Completed tasks" value={summary?.completed_tasks} note="Successfully finished" icon={CheckCircle2} tone="green" />
        <StatCard title="Pending tasks" value={summary?.pending_tasks} note="Waiting to be started" icon={Clock3} tone="orange" />
      </div>
      <section className="panel recent-panel">
        <div className="panel-heading"><div><h3>Recent tasks</h3><p className="muted">The latest work added to your workspace</p></div><Link to="/tasks" className="text-link">View all <ArrowUpRight size={15}/></Link></div>
        <div className="table-wrap">
          <table><thead><tr><th>Task</th><th>Assigned to</th><th>Priority</th><th>Due date</th><th>Status</th></tr></thead>
            <tbody>{tasks.length ? tasks.map((task) => <tr key={task.id}><td><strong>{task.title}</strong><small className="cell-sub">{task.description || "No description"}</small></td><td>{task.employee_name || "Unassigned"}</td><td><span className={`priority ${task.priority.toLowerCase()}`}>{task.priority}</span></td><td>{task.due_date}</td><td><StatusBadge status={task.status}/></td></tr>) : <tr><td colSpan="5" className="empty-cell">No tasks yet. Create your first task to get started.</td></tr>}</tbody>
          </table>
        </div>
      </section>
      <div className="dashboard-bottom"><div className="tip-card"><div className="tip-symbol">✦</div><div><strong>Keep your team aligned</strong><p>Assign tasks to employees and update their progress to keep your dashboard current.</p></div></div><div className="mini-stat"><span>In progress</span><strong>{summary?.in_progress_tasks ?? "—"}</strong><span className="mini-caption">Tasks currently underway</span></div></div>
    </>
  );
}
