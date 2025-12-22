
---

# Employee Directory System

---

## Introduction

This repository contains a full-stack Employee Directory application developed using **FastAPI**, **MySQL**, **Python** and **React**. The purpose of this project is to demonstrate practical backend architecture, frontend integration, and overall application design rather than focusing on excessive features.

The application allows users to search employee records by name or department and view the results in a structured grid layout. The project emphasizes clean code, maintainability, and clear separation of concerns between system layers.

This repository is intended to be readable and reusable by other developers in the future.

---

## Technology Stack

### Backend

* **FastAPI** – Used to build RESTful APIs
* **SQLAlchemy** – ORM used for database interaction
* **MySQL** – Relational database
* **Pydantic** – Data validation and serialization
* **python-dotenv** – Environment variable management

### Frontend

* **React (Vite)** – Frontend framework
* **JavaScript (ES6)** – Application logic
* **CSS** – Layout, styling, and animations

### Development Tools

* Git
* Node.js
* npm
* Python virtual environment

---
## System Requirements

To run this project locally, the following system requirements are recommended.

* Operating System

* Windows 10 or later

* macOS 12 or later

* Linux (Ubuntu 20.04+ recommended)

## Hardware

* Minimum 8 GB RAM (recommended for smooth MySQL and frontend runtime)

* Minimum 10 GB free disk space

## Software Requirements
### Backend

* Python 3.10 or later

* MySQL Server 8.0 or later

* pip (Python package manager)

### Frontend

* Node.js 18 or later

* npm 9 or later

### Tools

* Git

* Any modern web browser (Chrome, Edge, Firefox)

---

## Project Structure

```
Huzaifa-Zahid-Shah-Assignment/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   └── database.py
│   │   ├── models/
│   │   │   └── employee.py
│   │   ├── repositories/
│   │   │   └── employee_repo.py
│   │   ├── services/
│   │   │   └── employee_service.py
│   │   ├── routers/
│   │   │   └── employee_router.py
│   │   └── main.py
│   │
│   ├── scripts/
│   │   └── seed_employees.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.jsx
│   │   │   ├── EmployeeList.jsx
│   │   │   └── EmployeeCard.jsx
│   │   ├── services/
│   │   │   └── employeeApi.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

## Backend Design and Architecture

The backend is structured using a layered architecture to ensure clarity, scalability, and ease of maintenance.

### Database Layer

The database connection is configured in `database.py`. SQLAlchemy is used to manage connections and sessions. A shared base class is defined for all ORM models.

This approach ensures consistent database access throughout the application and allows dependency injection of database sessions into API routes.

---

### Model Layer

The `Employee` model defines the structure of the employees table. It includes fields such as name, email, department, designation, and date of joining.

Using ORM models allows schema validation, safer database queries, and reusability across the application, including scripts and API logic.

---

### Repository Layer

The repository layer is responsible only for interacting with the database. It contains functions that construct and execute SQLAlchemy queries.

No business logic or validation is performed here. This separation allows the data access logic to remain isolated and easily testable.

---

### Service Layer

The service layer acts as an intermediary between the API routes and the repository. It performs validation and applies business rules before interacting with the database.

For example, search input is validated before executing database queries. This keeps API routes clean and ensures consistent logic across the application.

---

### Router Layer

The router layer handles HTTP requests and responses. It extracts query parameters, injects dependencies, and returns JSON responses to the frontend.

All routes are grouped logically and registered in the main application file.

---

### Application Entry Point

The `main.py` file initializes the FastAPI application, registers routers, configures middleware, and creates database tables at startup if they do not already exist.

---

## Database Choice

This project uses MySQL as the database.

Reason for Choosing MySQL

1. MySQL is a widely used relational database in production systems.

2. It provides strong consistency and structured schema enforcement.

3. It is well suited for employee and organizational data.

4. It integrates seamlessly with SQLAlchemy ORM.

5. The relational nature of employee data (name, department, designation, joining date) makes MySQL an appropriate choice compared to document-based databases.

6. SQLAlchemy is used as an abstraction layer so that the database can be changed in the future without rewriting application logic.

--- 

## Seed Script

The project includes a Python seed script that generates 50 realistic employee records.

This script:

* Uses ORM models
* Prevents duplicate inserts
* Generates meaningful test data
* Can be run multiple times safely

Seed scripts are intentionally kept outside the application code to avoid mixing runtime logic with development utilities.

---

## Frontend Design and Architecture

The frontend is built using React with a focus on simplicity and clarity.

### Application Flow

1. The user enters a search term.
2. The input value is controlled by React state.
3. A debounced effect triggers an API call.
4. The backend returns matching employees.
5. Results are rendered in a grid layout.

---

### Component Structure

* **SearchBar**
  Handles user input and passes the value to the parent component.

* **EmployeeList**
  Responsible for layout and rendering multiple employee cards.

* **EmployeeCard**
  Displays individual employee details in a structured format.

Each component has a single responsibility, making the UI easy to maintain and extend.

---

### Layout and Styling

CSS Grid is used to display employees in a three-column layout on larger screens. The layout adjusts automatically for smaller screen sizes.

Animations are implemented using basic CSS transitions to improve user experience without introducing external libraries.

---

## Search Performance Optimization (Conceptual)

The employee search feature is optimized both on the frontend and backend to ensure efficient performance.

### Frontend Optimization

The search input is debounced.

1. API calls are delayed by a short interval after typing stops.

2. This prevents sending a request on every keystroke.

3. It reduces unnecessary network traffic and backend load.

4. As a result, the application remains responsive even with rapid user input.

### Backend Optimization

1. The search query uses indexed database columns (name and department).

2. Case-insensitive partial matching is handled at the database level.

3. Only relevant rows are returned instead of fetching all records.

4. The backend performs filtering directly in the database rather than in application memory, which improves scalability as the dataset grows.

---

## Installation and Setup

This section describes the complete setup process required to run the project locally. Both backend and frontend must be running simultaneously.

### Backend Setup
* Step 1: Navigate to the backend directory
`cd backend`

* Step 2: Create a Python virtual environment
`python -m venv venv`

* Step 3: Activate the virtual environment

Windows

`venv\Scripts\activate`


macOS / Linux

`source venv/bin/activate`

* Step 4: Install backend dependencies
`pip install -r requirements.txt`

* Step 5: Configure environment variables

1. Create a  `.env` file inside the backend directory using the example below:

`DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=employee_db`


2. Make sure the MySQL database specified above already exists.

* Step 6: Start the backend server
`python -m uvicorn app.main:app --reload`


Once started, the backend will be available at:

`http://127.0.0.1:8000`


API documentation can be accessed at:

`http://127.0.0.1:8000/docs`

## Database Seeding

1. To populate the database with sample employee data, run the following command:

`cd backend
python -m scripts.seed_employees`


2. This script inserts 50 realistic employee records and is safe to run multiple times.

### Frontend Setup
Step 1: Navigate to the frontend directory
`cd frontend`

### Step 2: Install frontend dependencies
`npm install`

### Step 3: Start the frontend development server
`npm run dev`

The frontend application will be available at:

`http://localhost:5173`

## Running the Application

To use the application correctly:

1. Ensure the backend server is running on port `8000`

2. Ensure the frontend server is running on port `5173`

3. Open the frontend URL in a web browser

4. Use the search input to query employees by name or department

---

## Setup Steps

This project is structured so that both backend and frontend can be set up independently and run together.

### Backend Setup Summary

1. Clone the repository and navigate to the backend directory.

2. Create and activate a Python virtual environment.

3. Install backend dependencies from requirements.txt.

4. Configure database credentials using environment variables.

5. Start the FastAPI server using Uvicorn.

6. Seed the database with sample employee data.

7. Once started, the backend exposes a REST API on port 8000 which the frontend consumes.

### Frontend Setup Summary

1. Navigate to the frontend directory.

2. Install dependencies using npm.

3. Start the Vite development server.

4. The frontend runs on port 5173 and communicates with the backend using HTTP requests.

5. Both servers must be running simultaneously for the application to work correctly.

---

## How the System Works End-to-End

* The frontend captures user input.
* Requests are sent to the backend API.
* The backend processes the request through multiple layers.
* The database returns matching records.
* The frontend renders results in a structured layout.

---

## Application Screenshots
### Initial Search Interface

This view shows the application on initial load with the search input centered and ready for user interaction.
![Initial Search Screen](docs/output1.JPG)
### Search by Employee Name

This example shows the results returned when searching by an employee’s name. Matching records are displayed in a three-column grid layout.

![Search by Name](docs/output2.JPG)

![Search by Name](docs/output3.JPG)

### Search by Department

This example demonstrates searching employees by department. The results dynamically update based on the query.

![Search by Department](docs/output4.JPG)

---

