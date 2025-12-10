# deep-learning-ninja

Personal workspace for:
- **Machine Learning Zoomcamp**
- **Dive into Deep Learning (D2L)**

## Layout

- `ml_zoomcamp/` – notes, notebooks, and code following the ML Zoomcamp course
- `d2l/` – notebooks and experiments following the D2L book
- `notebooks/` – ad-hoc experiments not tied to a single course
- `src/` – reusable Python modules shared across projects
- `data/` – data directories (kept out of git by default)
- `experiments/` – experiment configs, logs, and outputs

## Environment

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Then open the folder in VS Code and select the `.venv` interpreter.
