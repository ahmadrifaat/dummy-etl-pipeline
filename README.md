## Dependencies / Script and Test Run Instruction

Libraries used in this project:

```text
pandas~=2.2
beautifulsoup4~=4.12
requests~=2.32
sqlalchemy>=2.0
psycopg2-binary~=2.9
pg8000
gspread
google-api-python-client~=2.152
google-auth~=2.36
pytest~=8.0
pytest-cov~=6.0

```bash
Run ETL Pipeline script
python main.py

run unit test
python -m pytest tests/

run test coverage
python -m coverage run -m pytest tests/
python -m coverage report -m

# URL Google Sheets:
[https://docs.google.com/spreadsheets/d/1da_S99NcBK1UrJh8vPhw51C88tiDtf_FwpZX4RTnmCU/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1da_S99NcBK1UrJh8vPhw51C88tiDtf_FwpZX4RTnmCU/edit?usp=sharing)

