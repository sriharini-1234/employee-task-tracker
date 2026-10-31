def test_employee_task_workflow(client):
    employee_response = client.post(
        "/api/employees/",
        json={"name": "Asha Rao", "email": "asha@example.com", "department": "Engineering"},
    )
    assert employee_response.status_code == 201
    employee = employee_response.json()

    task_response = client.post(
        "/api/tasks/",
        json={
            "title": "Build login page",
            "description": "Create the login UI",
            "priority": "High",
            "due_date": "2030-05-20",
            "employee_id": employee["id"],
        },
    )
    assert task_response.status_code == 201
    task = task_response.json()
    assert task["employee_name"] == "Asha Rao"
    assert task["status"] == "Pending"

    update_response = client.patch(
        f"/api/tasks/{task['id']}/status",
        json={"status": "Completed"},
    )
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "Completed"

    dashboard = client.get("/api/dashboard").json()
    assert dashboard["total_employees"] == 1
    assert dashboard["total_tasks"] == 1
    assert dashboard["completed_tasks"] == 1


def test_duplicate_employee_email_returns_conflict(client):
    payload = {"name": "Asha Rao", "email": "asha@example.com", "department": "Engineering"}
    assert client.post("/api/employees/", json=payload).status_code == 201
    assert client.post("/api/employees/", json=payload).status_code == 409
