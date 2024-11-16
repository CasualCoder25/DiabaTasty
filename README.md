## Steps to run the backend

### For Localhost Setup
- Create a /app/local_secrets.py file
- Add `GOOGLE_API_KEY` as a variable
- Add `model_name` as a variable

### For Deployment Setup
- Add `GOOGLE_API_KEY` as a environemnt variable
- Add `model_name` as a environemnet variable

### Create vitual environemnt and installing dependencies
- With in source folder, open terminal and execute `python -m env venv`
- With in source folder, open terminal and activate venv by executing `venv/Scripts/Activate`
- Now execute `pip install -r requirements.txt` in the activated venv

### Running the server on localhost with reload on change
- Open terminal in source folder and execute `uvicorn main:app --reload`

### API endpoint
- `POST: SOURCE_URL/get-recipe/`
- Visit `SOURCE_URL/docs` for input, output formats and further API documentations