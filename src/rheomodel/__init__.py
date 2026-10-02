"""rheomodel — rheological constitutive models with verified academic citations.

Pure science: equations, parameters, bounds, citations. Fitting machinery
(initial guesses, ladder seeding, robust regression) lives in rheofit.
"""

from .models import MODELS

__version__ = "0.1.0"


def list_models() -> list:
    """Names of all available models, sorted."""
    return sorted(MODELS)


def get_model(name: str):
    """Return the model module for *name* (raises KeyError if unknown)."""
    return MODELS[name]


__all__ = ["MODELS", "list_models", "get_model", "__version__"]
