# StatMuse Clone

A natural language interface for querying NBA data — inspired by [StatMuse](https://www.statmuse.com/). Ask questions like:

"How many points did LeBron average in 2023?"

This project uses Python and PostgreSQL to enable intelligent querying of structured basketball data.

---

## Features

- NLP to SQL query translation (in progress)
- Modular ETL pipeline using `extract/` and `load/` scripts
- Data stored in PostgreSQL (hosted on Aiven)
- Fuzzy string matching with `pg_trgm` and `fuzzystrmatch`
- Structured schema: `players`, `teams`, `games`, and more
- Optional: Airflow integration for scheduled data updates

---

## Project Structure

