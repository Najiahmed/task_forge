<<<<<<< HEAD
# task_forge
this is a fastapi project for learning
=======
# TaskForge API

Current learning-stage architecture:

- FastAPI
- APIRouter
- Pydantic schemas
- Service layer
- Repository layer
- In-memory storage
- CRUD endpoints

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## Current routes

- GET /tasks
- GET /tasks/{task_id}
- POST /tasks
- PATCH /tasks/{task_id}
- DELETE /tasks/{task_id}

PostgreSQL / SQLAlchemy integration is the next course step.
>>>>>>> f985c67 (feat: create project)
