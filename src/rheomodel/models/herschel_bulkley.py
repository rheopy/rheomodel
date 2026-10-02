"""
Herschel-Bulkley — yield stress + power-law flow
  σ = σ_y + K·γ̇ⁿ

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "herschel_bulkley"
PARAMS = ['sigma_y', 'K', 'n']
SCORECARD_PARAMS = ['sigma_y', 'K', 'n']
LOG_PARAMS = ('sigma_y', 'K')
BOUNDS = {
    "sigma_y": (1e-12, np.inf),
    "K": (1e-12, np.inf),
    "n": (0.01, 2.0),
}
# n -> 1 recovers Bingham
PARENT = 'bingham'
PARENT_EXACT = True
CITATION = {
    "authors": 'Herschel, W. H., & Bulkley, R.',
    "year": 1926,
    "title": 'Konsistenzmessungen von Gummi-Benzollösungen',
    "journal": 'Kolloid-Zeitschrift',
    "volume": '39(4)',
    "pages": '291-300',
    "doi": '10.1007/BF01432034',
}
PARAM_INFO = {
    "sigma_y": {"symbol": "σ_y", "unit": "Pa", "description": "Yield stress"},
    "K": {"symbol": "K", "unit": "Pa·sⁿ", "description": "Consistency index (for Bingham/Casson: plastic viscosity)"},
    "n": {"symbol": "n", "unit": "–", "description": "Flow behavior index"},
}

def equation(gamma_dot, sigma_y, K, n):
    return sigma_y + K * gamma_dot ** n

def get_equation_latex() -> str:
    return "σ = σ_y + K·γ̇ⁿ"
