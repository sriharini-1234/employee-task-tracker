import { useEffect, useState } from "react";
import { ClipboardList, Search, Trash2 } from "lucide-react";
import { addTask, deleteTask, getEmployees, getTasks, getErrorMessage, updateTaskStatus } from "../api";
import StatusBadge from "../components/StatusBadge";

const initialForm = { title: "", description: "", priority: "Medium", due_date: "", employee_id: "" };
const statuses = ["Pending", "In Progress", "Completed"];

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState(initialForm);
  const [filter, setFilter] = useState("");
  const [search, setSearch] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [busy, setBusy] = useState(false);

  async function loadTasks() {
    try { const response = await getTasks({ ...(filter ? { status: filter } : {}), ...(search ? { search } : {}) }); setTasks(response.data); }
    catch (err) { setError(getErrorMessage(err)); }
  }
  async function loadEmployees() {
    try { const response = await getEmployees(); setEmployees(response.data); }
    catch (err) { setError(getErrorMessage(err)); }
  }
  useEffect(() => { loadEmployees(); }, []);
  useEffect(() => { loadTasks(); }, [filter, search]);

  function change(e) { setForm({ ...form, [e.target.name]: e.target.value }); }

  async function submit(e) {
    e.preventDefault(); setError(""); setSuccess(""); setBusy(true);
    try {
      await addTask({ ...form, employee_id: Number(form.employee_id) });
      setForm(initialForm); setSuccess("Task created and assigned successfully."); await loadTasks();
    } catch (err) { setError(getErrorMessage(err)); }
    finally { setBusy(false); }
  }

  async function changeStatus(id, status) {
    try { await updateTaskStatus(id, status); setSuccess("Task status updated."); await loadTasks(); }
    catch (err) { setError(getErrorMessage(err)); }
  }

  async function remove(id) {
    if (!window.confirm("Delete this task?")) return;
    try { await deleteTask(id); setSuccess("Task deleted."); await loadTasks(); }
    catch (err) { setError(getErrorMessage(err)); }
  }

  return (
    <>
      <div className="page-heading"><div><p className="eyebrow">WORK MANAGEMENT</p><h2>Tasks</h2><p className="muted">Create, assign and track your team's work.</p></div><div className="count-pill"><ClipboardList size={16}/>{tasks.length} tasks shown</div></div>
      {error && <div className="alert error">{error}</div>}{success && <div className="alert success">{success}</div>}
      <section className="panel form-panel task-form-panel">
        <div className="panel-heading"><div><h3>Create a new task</h3><p className="muted">Add the task details and choose an employee.</p></div></div>
        <form onSubmit={submit} className="task-form">
          <label>Task title<input name="title" value={form.title} onChange={change} placeholder="e.g. Prepare monthly report" minLength="2" required /></label>
          <label>Assign to<select name="employee_id" value={form.employee_id} onChange={change} required><option value="">Select employee</option>{employees.map((employee) => <option key={employee.id} value={employee.id}>{employee.name}</option>)}</select></label>
          <label>Description<textarea name="description" value={form.description} onChange={change} placeholder="Add task details..." rows="2" /></label>
          <div className="form-row">
            <label>Priority<select name="priority" value={form.priority} onChange={change}><option>Low</option><option>Medium</option><option>High</option></select></label>
            <label>Due date<input name="due_date" type="date" value={form.due_date} onChange={change} required /></label>
          </div>
          <div className="form-actions"><button className="primary-button" disabled={busy || employees.length === 0}>{busy ? "Creating..." : "＋ Create task"}</button>{employees.length === 0 && <span className="muted form-hint">Add an employee before creating a task.</span>}</div>
        </form>
      </section>
      <section className="panel tasks-panel">
        <div className="panel-heading"><div><h3>Task list</h3><p className="muted">View and update task progress.</p></div></div>
        <div className="task-toolbar">
          <div className="search-box"><Search size={17}/><input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search tasks..." /></div>
          <select className="filter-select" value={filter} onChange={(e) => setFilter(e.target.value)}><option value="">All statuses</option>{statuses.map((status) => <option key={status}>{status}</option>)}</select>
        </div>
        <div className="table-wrap"><table><thead><tr><th>Task</th><th>Assigned employee</th><th>Priority</th><th>Due date</th><th>Status</th><th>Action</th></tr></thead><tbody>
          {tasks.length ? tasks.map((task) => <tr key={task.id}><td><strong>{task.title}</strong><small className="cell-sub">{task.description || "No description"}</small></td><td>{task.employee_name || "Unassigned"}</td><td><span className={`priority ${task.priority.toLowerCase()}`}>{task.priority}</span></td><td>{task.due_date}</td><td><select className={`status-select ${task.status === "Completed" ? "status-done" : task.status === "In Progress" ? "status-working" : ""}`} value={task.status} onChange={(e) => changeStatus(task.id, e.target.value)}>{statuses.map((status) => <option key={status}>{status}</option>)}</select></td><td><button className="icon-button danger-button" title="Delete task" onClick={() => remove(task.id)}><Trash2 size={16}/></button></td></tr>) : <tr><td colSpan="6" className="empty-cell">No tasks match your filters. Create a task to get started.</td></tr>}
        </tbody></table></div>
      </section>
    </>
  );
}
