# Y_LAB_MENU
_______
1. Install environment -- "python -m venv venv"
2. Activate environment -- "source venv/scripts/activate"
3. Install requirements -- "pip install -r requirements.txt"
4. Create file ".env"
5. .env example:
- 1. DATABASE_URL=postgresql://postgres:meddyson888@db:5432/resturant
- 2.  DB_USER=postgres
- 3.  DB_PASSWORD=meddyson888
- 4.  DB_NAME=resturant
6. Run docker compose(docker-compose up -d)
7. Run container with tests(docker-compose -f"docker-compose.test.yaml" up)

