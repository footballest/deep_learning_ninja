import pathlib
from typing import Union

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]


def project_path(*parts: Union[str, pathlib.Path]) -> pathlib.Path:
    """Convenience helper to get an absolute path inside the project.

    Example:
        project_path("data", "raw", "file.csv")
    """
    return PROJECT_ROOT.joinpath(*parts)
