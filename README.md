# cloud44-demo

A small notes board on Flask and PostgreSQL: the repository Cloud44 reads in our DevSecOps22 class demo.
Paste `https://github.com/guyshonshon/cloud44-demo` into Cloud44 and it reads a Python app using PostgreSQL,
asks what it cannot tell, scores where it should run, and writes the infrastructure.

Run it locally:

```bash
docker compose up
```

Then open http://localhost:8000.

- `app.py`: the app (routes `/`, `POST /notes`, `/healthz`), database from `DATABASE_URL`.
- `boot.sh`: creates the table, then serves with gunicorn.
- `Dockerfile`: the image, a non-root user.
