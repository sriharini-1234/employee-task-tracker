import { useEffect, useState } from "react";
import { Search, Trash2, UserPlus, Users } from "lucide-react";
import { addEmployee, deleteEmployee, getEmployees, getErrorMessage } from "../api";

const emptyForm = { name: "", email: "", department: "" };

export default function Employees() {
  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState(emptyForm);
  const [search, setSearch] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [busy, setBusy] = useState(false);

  async function loadEmployees(term = search) {
    try { const response = await getEmployees(term); setEmployees(response.data); }
    catch (err) { setError(getErrorMessage(err)); }
  }
  useEffect(() => { loadEmployees(""); }, []);

  function change(e) { setForm({ ...form, [e.target.name]: e.target.value }); }

  async function submit(e) {
    e.preventDefault(); setError(""); setSuccess(""); setBusy(true);
    try {
      await addEmployee(form);
      setForm(emptyForm); setSuccess("Employee added successfully."); await loadEmployees();
    } catch (err) { setError(getErrorMessage(err)); }
    finally { setBusy(false); }
  }

  async function remove(id, name) {
    if (!window.confirm(`Delete ${name}? Their tasks will remain but become unassigned.`)) return;
    setError(""); setSuccess("");
    try { await deleteEmployee(id); setSuccess("Employee deleted."); await loadEmployees(); }
    catch (err) { setError(getErrorMessage(err)); }
  }

  return (
    <>
      <div className="page-heading"><div><p className="eyebrow">YOUR TEAM</p><h2>Employees</h2><p className="muted">Add and manage the people in your workspace.</p></div><div className="count-pill"><Users size={16}/>{employees.length} employees</div></div>
      {error && <div className="alert error">{error}</div>}{success && <div className="alert success">{success}</div>}
      <div className="content-grid">
        <section className="panel form-panel">
          <div className="panel-heading"><div><h3>Add employee</h3><p className="muted">Enter the employee's details below.</p></div><div className="small-icon"><UserPlus size={18}/></div></div>
          <form onSubmit={submit} className="stack-form">
            <label>Full name<input name="name" value={form.name} onChange={change} placeholder="e.g. Priya Sharma" minLength="2" required /></label>
            <label>Email address<input name="email" type="email" value={form.email} onChange={change} placeholder="name@company.com" required /></label>
            <label>Department<input name="department" value={form.department} onChange={change} placeholder="e.g. Engineering" minLength="2" required /></label>
            <button className="primary-button full-button" disabled={busy}>{busy ? "Adding..." : "＋ Add employee"}</button>
          </form>
        </section>
        <section className="panel list-panel">
          <div className="panel-heading"><div><h3>Employee directory</h3><p className="muted">All registered employees</p></div></div>
          <div className="search-box"><Search size={17}/><input value={search} onChange={(e) => { setSearch(e.target.value); loadEmployees(e.target.value); }} placeholder="Search by employee name..." /></div>
          <div className="employee-list">
            {employees.length ? employees.map((employee) => <div className="employee-row" key={employee.id}><div className="avatar employee-avatar">{employee.name.charAt(0).toUpperCase()}</div><div className="employee-info"><strong>{employee.name}</strong><span>{employee.email}</span></div><span className="department-tag">{employee.department}</span><button className="icon-button danger-button" title="Delete employee" onClick={() => remove(employee.id, employee.name)}><Trash2 size={17}/></button></div>) : <div className="empty-state">No employees found. Add an employee to get started.</div>}
          </div>
        </section>
      </div>
    </>
  );
}
