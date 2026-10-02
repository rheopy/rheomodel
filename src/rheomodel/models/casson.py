"""
Casson — yield stress with square-root blending
  √σ = √σ_y + √(K·γ̇)

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "casson"
PARAMS = ['sigma_y', 'K']
SCORECARD_PARAMS = ['sigma_y', 'K']
LOG_PARAMS = ('sigma_y', 'K')
BOUNDS = {
    "sigma_y": (1e-12, np.inf),
    "K": (1e-12, np.inf),
}
PARENT = None
CITATION = {
    "authors": 'Casson, N.',
    "year": 1959,
    "title": 'A flow equation for pigment-oil suspensions of the printing ink type',
    "journal": 'Rheology of Disperse Systems (ed. C. Mill), Pergamon Press',
    "volume": None,
    "pages": '84-104',
    "doi": None,
}
PARAM_INFO = {
    "sigma_y": {"symbol": "σ_y", "unit": "Pa", "description": "Yield stress"},
    "K": {"symbol": "K", "unit": "Pa·sⁿ", "description": "Consistency index (for Bingham/Casson: plastic viscosity)"},
}

def equation(gamma_dot, sigma_y, K):
    return (np.sqrt(sigma_y) + np.sqrt(K * gamma_dot)) ** 2

def get_equation_latex() -> str:
    return "√σ = √σ_y + √(K·γ̇)"
