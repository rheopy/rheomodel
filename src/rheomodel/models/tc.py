"""
TC — Two-Component (yield stress + Newtonian background)
  σ = σ_y + σ_y·(γ̇/γ̇_c)^½ + η_bg·γ̇

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "tc"
PARAMS = ['sigma_y', 'gamma_dot_c', 'eta_bg']
SCORECARD_PARAMS = ['sigma_y', 'eta_bg']
LOG_PARAMS = ('sigma_y', 'gamma_dot_c', 'eta_bg')
BOUNDS = {
    "sigma_y": (1e-12, np.inf),
    "gamma_dot_c": (1e-06, np.inf),
    "eta_bg": (1e-12, np.inf),
}
PARENT = None
CITATION = {
    "authors": 'Caggioni, M., Trappe, V., & Spicer, P. T.',
    "year": 2020,
    "title": 'Variations of the Herschel-Bulkley exponent reflecting contributions of the viscous continuous phase to the shear rate-dependent stress of soft glassy materials',
    "journal": 'Journal of Rheology',
    "volume": '64(2)',
    "pages": '413-422',
    "doi": '10.1122/1.5120633',
}
PARAM_INFO = {
    "sigma_y": {"symbol": "σ_y", "unit": "Pa", "description": "Yield stress"},
    "gamma_dot_c": {"symbol": "γ̇_c", "unit": "s⁻¹", "description": "Critical shear rate of the elastoplastic transition"},
    "eta_bg": {"symbol": "η_bg", "unit": "Pa·s", "description": "Background (high-shear) viscosity"},
}

def equation(gamma_dot, sigma_y, gamma_dot_c, eta_bg):
    return sigma_y + sigma_y * np.sqrt(gamma_dot / gamma_dot_c) + eta_bg * gamma_dot

def get_equation_latex() -> str:
    return "σ = σ_y + σ_y·(γ̇/γ̇_c)^½ + η_bg·γ̇"
