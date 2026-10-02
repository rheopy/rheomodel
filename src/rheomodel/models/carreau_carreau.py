"""
Carreau–Carreau — two Carreau modes (advisory combination)

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "carreau_carreau"
PARAMS = ['eta_0_1', 'lambda_val_1', 'eta_0_2', 'lambda_val_2']
SCORECARD_PARAMS = ['eta_0_1', 'eta_0_2']
LOG_PARAMS = ('eta_0_1', 'lambda_val_1', 'eta_0_2', 'lambda_val_2')
BOUNDS = {
    "eta_0_1": (1e-12, np.inf),
    "lambda_val_1": (1e-12, np.inf),
    "eta_0_2": (1e-12, np.inf),
    "lambda_val_2": (1e-12, np.inf),
}
# advisory only: fixed -1/4, -1/2 exponents
PARENT = 'carreau'
PARENT_EXACT = False
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
    "eta_0_1": {"symbol": "η₀,₁", "unit": "Pa·s", "description": "Zero-shear viscosity, first Carreau mode"},
    "lambda_val_1": {"symbol": "λ₁", "unit": "s", "description": "Relaxation time, first Carreau mode"},
    "eta_0_2": {"symbol": "η₀,₂", "unit": "Pa·s", "description": "Zero-shear viscosity, second Carreau mode"},
    "lambda_val_2": {"symbol": "λ₂", "unit": "s", "description": "Relaxation time, second Carreau mode"},
}

def equation(gamma_dot, eta_0_1, lambda_val_1, eta_0_2, lambda_val_2):
    c1 = eta_0_1 * gamma_dot * (1.0 + (lambda_val_1 * gamma_dot) ** 2) ** (-0.25)
    c2 = eta_0_2 * gamma_dot * (1.0 + (lambda_val_2 * gamma_dot) ** 2) ** (-0.5)
    return c1 + c2

def get_equation_latex() -> str:
    return "σ = η₀,₁·γ̇·[1+(λ₁·γ̇)²]^(-¼) + η₀,₂·γ̇·[1+(λ₂·γ̇)²]^(-½)"
