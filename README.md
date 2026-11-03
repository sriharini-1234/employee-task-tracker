# Employee Task Tracker

Employee Task Tracker (also called TaskFlow in the app) is a small web application for keeping track of employees and the work assigned to them. This guide is written for someone setting up the project for the first time on Windows.

## What you can do

- View a dashboard with employee and task totals.
- Add, search, update, and delete employees.
- Create, search, edit, and delete tasks.
- Assign a task to an employee and change its status.
- Filter tasks by status.
- Keep tasks when an employee is deleted; those tasks become unassigned.

## How the project works

The project has three parts:

1. **Frontend** (`frontend/`): the website you open in your browser. It is built with React and Vite.
2. **Backend** (`backend/`): the API that handles requests. It is built with Python and FastAPI.
3. **Database**: PostgreSQL stores employee and task data. SQLAlchemy connects the backend to the database.

The browser sends requests to the backend, and the backend reads or changes data in PostgreSQL. While developing, keep the frontend and backend running in two separate terminal windows.

# Employee Task Tracker

A full-stack web application designed to manage employees, assign tasks, track task progress and monitor overall work through a dashboard.

Built using **React.js, Python FastAPI and PostgreSQL**.

---

## 1. Project Overview

The Employee Task Tracker is a web-based application that helps organizations manage employee information and daily tasks efficiently.

Instead of maintaining employee and task details manually, users can manage everything through a single dashboard.

### Main objectives

- Manage employee information.
- Create and assign tasks to employees.
- Track task completion status.
- Update employee and task details.
- Monitor overall progress through dashboard statistics.
- Store application data in a PostgreSQL database.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| React.js | Frontend user interface |
| JavaScript | Frontend functionality |
| HTML | Application structure |
| CSS | Application styling |
| Python | Backend programming |
| FastAPI | REST API development |
| PostgreSQL | Database management |
| SQLAlchemy | Database ORM |
| Pydantic | Data validation |
| Axios | Frontend API communication |
| Uvicorn | FastAPI application server |
| Swagger UI | API documentation and testing |
| Git & GitHub | Version control |

## 3. Features

### A. Dashboard

The dashboard provides an overview of employee and task information.

It displays:

- Total employees.
- Total tasks.
- Completed tasks.
- Pending tasks.
- In-progress tasks.

### B. Employee Management

Users can manage employee information.

Available operations:

- Add a new employee.
- View all employees.
- Edit employee details.
- Delete an employee.
- Search employees.

Employee information includes:

- Employee name.
- Email address.
- Department.

### C. Task Management

Users can create and manage tasks.

Available operations:

- Create a new task.
- Assign tasks to employees.
- View all tasks.
- Edit task details.
- Delete tasks.
- Search tasks.
- Filter tasks by status.
- Update task status.

Task information includes:

- Task title.
- Description.
- Assigned employee.
- Priority.
- Due date.
- Task status.

### D. Task Status Management

Every task can have one of three statuses:

| Status | Meaning |
|---|---|
| Pending | Task has not started. |
| In Progress | Task is currently being worked on. |
| Completed | Task has been finished. |

### E. Task Priority

Tasks can be categorized based on priority:

- Low
- Medium
- High

---

## 4. Project Architecture

The application follows a client-server architecture.

```text
                 USER
                   |
                   v
          REACT FRONTEND
          (User Interface)
                   |
                   | HTTP Requests
                   | Axios
                   v
          FASTAPI BACKEND
          (REST APIs)
                   |
                   v
             SQLALCHEMY
             (ORM Layer)
                   |
                   v
            POSTGRESQL
              DATABASE
```

### How does the application work?

1. The user interacts with the React frontend.
2. React sends HTTP requests to FastAPI using Axios.
3. FastAPI receives the request through the appropriate API endpoint.
4. The backend validates incoming data using Pydantic schemas.
5. SQLAlchemy communicates with PostgreSQL.
6. PostgreSQL stores or retrieves the requested information.
7. FastAPI returns a response in JSON format.
8. React displays the updated information to the user.

---

## 5. Project Folder Structure

```text
employee-task-tracker/
│
├── backend/
│   │
│   ├── routers/
│   │   ├── employees.py
│   │   └── tasks.py
│   │
│   ├── tests/
│   │
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   ├── main.jsx
│   │   └── styles.css
│   │
│   ├── package.json
│   └── index.html
│
├── README.md
└── .gitignore
```

### Understanding the Backend Files

**1. main.py**

This is the entry point of the FastAPI application.

Responsibilities:
- Create the FastAPI application.
- Configure CORS.
- Register employee and task routers.
- Initialize database tables during application startup.

**2. database.py**

Responsible for database connectivity.

It contains:
- PostgreSQL database connection.
- SQLAlchemy engine.
- Database session configuration.
- Database dependency used by API endpoints.

**3. models.py**

Defines database tables using SQLAlchemy ORM.

For example:
- Employee model.
- Task model.

A model represents the structure of a database table.

**4. schemas.py**

Defines the structure and validation rules for incoming and outgoing API data.

Examples:
- EmployeeCreate.
- EmployeeUpdate.
- EmployeeOut.
- TaskCreate.
- TaskUpdate.
- TaskOut.
- TaskStatusUpdate.

**5. routers/employees.py**

Contains employee-related API endpoints.

Responsibilities:
- Create employees.
- Retrieve employees.
- Update employee details.
- Delete employees.

**6. routers/tasks.py**

Contains task-related API endpoints.

Responsibilities:
- Create tasks.
- Retrieve tasks.
- Update task details.
- Change task status.
- Delete tasks.
- Search and filter tasks.

**7. requirements.txt**

Contains Python dependencies required by the backend.

### Understanding the Frontend Files

**1. main.jsx**

The entry point of the React application.

It renders the main React component.

**2. App.jsx**

Defines the main application layout and page structure.

**3. api.js**

Contains Axios configuration and API functions.

It connects React with FastAPI.

**4. components/**

Contains reusable UI components such as:
- StatCard.
- StatusBadge.

**5. pages/**

Contains application pages such as:
- Dashboard.
- Employees.
- Tasks.

**6. styles.css**

Contains application styling, layouts, colors and responsive design.

---

## 6. Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Install the following software:

1. Python 3.12
2. Node.js and npm
3. PostgreSQL
4. Visual Studio Code
5. Git

### Step 1: Clone the repository

Open PowerShell or the VS Code terminal.

```bash
git clone https://github.com/sriharini-1234/employee-task-tracker.git
```

Navigate into the project:

```bash
cd employee-task-tracker
```

### Step 2: Set up the PostgreSQL database

Open PostgreSQL and create a database.

Example:

```sql
CREATE DATABASE employee_task_tracker;
```

Configure the database connection in the backend `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/employee_task_tracker
```

Replace `YOUR_PASSWORD` with your actual PostgreSQL password.

Never upload your actual `.env` file or database password to GitHub.

### Step 3: Set up the backend

Navigate to the backend folder:

```bash
cd backend
```

Create a Python virtual environment:

```bash
py -3.12 -m venv .venv312
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv312\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will run at:

http://127.0.0.1:8000

The API documentation is available at:

http://127.0.0.1:8000/docs

**Note:** The application initializes its database tables through the backend startup configuration. If your local version uses a separate initialization script, follow that script's instructions instead.

### Step 4: Set up the frontend

Open another terminal.

Navigate to the frontend folder:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

The frontend will usually run at:

http://localhost:5173

---

## 7. Deploying the frontend to Vercel

The frontend and FastAPI backend must both be deployed and reachable over HTTPS.
Deploying the Vite frontend to Vercel does **not** deploy the backend or database;
host those separately on a platform that supports FastAPI and PostgreSQL.

1. Import the repository in Vercel and set the project **Root Directory** to
   `frontend`. Use `npm run build` as the build command and `dist` as the output
   directory.
2. In the Vercel project settings, add the environment variable
   `VITE_API_URL` for each environment you deploy (Production, Preview, and/or
   Development). Set it to the public backend URL with `/api` at the end, for
   example `https://your-api-host.example.com/api`. Do not use `localhost` or
   a private network address. Redeploy after changing this variable.
3. In the backend hosting settings, set `DATABASE_URL` to the hosted PostgreSQL
   connection string and set `FRONTEND_ORIGIN` to the exact Vercel site origin,
   for example `https://your-project.vercel.app` (no trailing slash). For more
   than one frontend origin, separate the exact origins with commas. The API
   must allow the origin used by the browser, including Vercel preview origins
   if you use previews.
4. Start the backend with the host and port required by your hosting platform.
   For platforms that provide a `PORT` environment variable, a typical command
   from the `backend` directory is:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

5. Open the deployed API's `/` URL and confirm it returns the API running
   message. Then open the Vercel site and test the dashboard and employee/task
   requests.

The frontend's local default (`http://localhost:8000/api`) is only used during
Vite development. A deployed app without `VITE_API_URL` reports a clear
configuration error at startup instead of silently calling the visitor's computer.

---

## 8. API Endpoints

The backend provides REST APIs for employee and task management.

### Employee APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/employees/` | Create employee |
| GET | `/api/employees/` | Retrieve employees |
| PUT | `/api/employees/{employee_id}` | Update employee |
| DELETE | `/api/employees/{employee_id}` | Delete employee |

### Task APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/tasks/` | Create task |
| GET | `/api/tasks/` | Retrieve tasks |
| PUT | `/api/tasks/{task_id}` | Update task details |
| PATCH | `/api/tasks/{task_id}/status` | Update task status |
| DELETE | `/api/tasks/{task_id}` | Delete task |

### Dashboard API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/dashboard` | Retrieve dashboard statistics |

### Example API Request

Create an employee:

```json
{
  "name": "Sriharini",
  "email": "sriharini@example.com",
  "department": "IT"
}
```

Create a task:

```json
{
  "title": "Develop Employee Dashboard",
  "description": "Create the employee dashboard interface",
  "priority": "High",
  "due_date": "2026-11-05",
  "employee_id": 1
}
```

The employee ID must belong to an existing employee.

---

## 9. Testing the APIs

FastAPI automatically generates interactive API documentation using Swagger UI.

Open:

http://127.0.0.1:8000/docs

You can use Swagger to:

- Test GET requests.
- Create employees and tasks.
- Update employee information.
- Edit task details.
- Change task status.
- Delete records.
- View API responses and status codes.

You can also use Postman to test the REST APIs.

---

## 10. Important Concepts Used

| Concept | Explanation |
|---|---|
| React Components | Reusable parts of the user interface |
| useState | Manages component state |
| useEffect | Handles side effects such as API loading |
| REST API | Communication between frontend and backend |
| HTTP Methods | GET, POST, PUT, PATCH and DELETE |
| FastAPI Router | Organizes API endpoints |
| Pydantic | Validates request and response data |
| SQLAlchemy ORM | Interacts with database tables using Python objects |
| PostgreSQL | Relational database |
| Axios | Sends HTTP requests from React |
| CORS | Controls cross-origin browser requests |
| Swagger | Interactive API documentation |

---

## 11. Error Handling and Troubleshooting

### Backend does not start

Check:
- Python version.
- Virtual environment activation.
- Installed dependencies.
- Database connection settings.

### Database connection error

Check:
- PostgreSQL service is running.
- Database exists.
- Database username and password are correct.
- DATABASE_URL is configured correctly.

### Frontend cannot connect to backend

For a deployed site, check:

- The backend is deployed separately, running, and reachable at its public
  HTTPS URL.
- Vercel has `VITE_API_URL` set to the backend URL ending in `/api`, and the
  frontend was redeployed after setting it.
- The backend's `FRONTEND_ORIGIN` contains the exact site origin shown in the
  browser address bar, with no path or trailing slash.
- The backend's `DATABASE_URL` points to the hosted PostgreSQL database.
- The browser developer tools' Network tab shows the request going to the
  backend URL, not `localhost`. A CORS error usually means `FRONTEND_ORIGIN`
  does not match the deployed site origin; a failed network request can mean
  the backend URL is unreachable or the backend is not running.

For local development, confirm FastAPI is running at `http://localhost:8000`
and CORS allows `http://localhost:5173`.

### npm package errors

Run:

```bash
npm install
npm run dev
```

Run these commands from the frontend directory.

---

## 12. Running the Complete Project

You need two terminals.

**Terminal 1 – Backend**

```powershell
cd backend
.\.venv312\Scripts\Activate.ps1
uvicorn main:app --reload
```

**Terminal 2 – Frontend**

```powershell
cd frontend
npm run dev
```

Keep both terminals running while using the application.

---

## 13. Future Enhancements

Possible improvements for future versions:

- User authentication and authorization.
- Admin and employee roles.
- Employee profile management.
- Task deadline notifications.
- Advanced filtering and sorting.
- Pagination.
- Email notifications.
- Deployment to a cloud platform.
- Automated frontend and backend testing.

---

## 14. Learning Outcomes

By developing this project, I gained practical experience in:

- Building frontend applications using React.js.
- Developing REST APIs using Python FastAPI.
- Working with PostgreSQL databases.
- Implementing CRUD operations.
- Connecting frontend and backend applications.
- Using SQLAlchemy ORM.
- Validating API data using Pydantic.
- Testing APIs through Swagger UI.
- Managing project versions using Git and GitHub.

---

## 15. Author

**Sriharini Chennu**

GitHub: https://github.com/sriharini-1234

Project Repository: https://github.com/sriharini-1234/employee-task-tracker

---

## Conclusion

The Employee Task Tracker demonstrates how a full-stack web application can be developed by integrating React.js, FastAPI and PostgreSQL.

It provides a centralized solution for employee management, task assignment and progress tracking while demonstrating practical frontend, backend and database development concepts.