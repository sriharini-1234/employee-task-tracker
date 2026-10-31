export default function StatusBadge({ status }) {
  const className = status === "Completed" ? "completed" : status === "In Progress" ? "in-progress" : "pending";
  return <span className={`status-badge ${className}`}>{status}</span>;
}
