export default function StatCard({ title, value, note, icon: Icon, tone }) {
  return (
    <article className="stat-card">
      <div className={`stat-icon ${tone}`}><Icon size={21} /></div>
      <div className="stat-title">{title}</div>
      <div className="stat-value">{value ?? "—"}</div>
      <div className="stat-note">{note}</div>
    </article>
  );
}
