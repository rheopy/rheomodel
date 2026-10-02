"""
Carreau — Newtonian plateaus with power-law transition
  σ = η₀·γ̇·[1+(λ·γ̇)²]^((n-1)/2)

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "carreau"
PARAMS = ['eta_0', 'lambda_val', 'n']
SCORECARD_PARAMS = ['eta_0']
LOG_PARAMS = ('eta_0', 'lambda_val')
BOUNDS = {
    "eta_0": (1e-12, np.inf),
    "lambda_val": (1e-12, np.inf),
    "n": (0.01, 1.0),
}
PARENT = None
CITATION = {
    "authors": 'Carreau, P. J.',
    "year": 1972,
    "title": 'Rheological equations from molecular network theories',
    "journal": 'Transactions of the Society of Rheology',
    "volume": '16(1)',
    "pages": '99-127',
    "doi": '10.1122/1.549276',
}
PARAM_INFO = {
    "eta_0": {"symbol": "η₀", "unit": "Pa·s", "description": "Zero-shear viscosity"},
    "lambda_val": {"symbol": "λ", "unit": "s", "description": "Characteristic relaxation time"},
    "n": {"symbol": "n", "unit": "–", "description": "Flow behavior index"},
}

def equation(gamma_dot, eta_0, lambda_val, n):
    return eta_0 * gamma_dot * (1.0 + (lambda_val * gamma_dot) ** 2) ** ((n - 1.0) / 2.0)

def get_equation_latex() -> str:
    return "σ = η₀·γ̇·[1+(λ·γ̇)²]^((n-1)/2)"
