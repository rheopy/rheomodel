"""
Power law (Ostwald–de Waele) — no yield stress
  σ = K·γ̇ⁿ

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "power_law"
PARAMS = ['K', 'n']
SCORECARD_PARAMS = ['K', 'n']
LOG_PARAMS = ('K',)
BOUNDS = {
    "K": (1e-12, np.inf),
    "n": (0.01, 2.0),
}
PARENT = None
CITATION = {
    "authors": 'Ostwald, W.',
    "year": 1925,
    "title": 'Über die Geschwindigkeitsfunktion der Viskosität disperser Systeme. I.',
    "journal": 'Kolloid-Zeitschrift',
    "volume": '36',
    "pages": '99-117',
    "doi": '10.1007/BF01431449',
}
PARAM_INFO = {
    "K": {"symbol": "K", "unit": "Pa·sⁿ", "description": "Consistency index (for Bingham/Casson: plastic viscosity)"},
    "n": {"symbol": "n", "unit": "–", "description": "Flow behavior index"},
}

def equation(gamma_dot, K, n):
    return K * gamma_dot ** n

def get_equation_latex() -> str:
    return "σ = K·γ̇ⁿ"
