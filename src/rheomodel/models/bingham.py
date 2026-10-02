"""
Bingham plastic — yield stress + Newtonian flow
  σ = σ_y + μ_p·γ̇

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "bingham"
PARAMS = ['sigma_y', 'K']
SCORECARD_PARAMS = ['sigma_y', 'K']
LOG_PARAMS = ('sigma_y', 'K')
BOUNDS = {
    "sigma_y": (1e-12, np.inf),
    "K": (1e-12, np.inf),
}
PARENT = None
CITATION = {
    "authors": 'Bingham, E. C.',
    "year": 1922,
    "title": 'Fluidity and Plasticity',
    "journal": 'McGraw-Hill Book Company',
    "volume": None,
    "pages": None,
    "doi": None,
}
PARAM_INFO = {
    "sigma_y": {"symbol": "σ_y", "unit": "Pa", "description": "Yield stress"},
    "K": {"symbol": "K", "unit": "Pa·sⁿ", "description": "Consistency index (for Bingham/Casson: plastic viscosity)"},
}

def equation(gamma_dot, sigma_y, K):
    return sigma_y + K * gamma_dot

def get_equation_latex() -> str:
    return "σ = σ_y + μ_p·γ̇"
