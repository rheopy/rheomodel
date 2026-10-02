"""
TC-Carreau — yield stress + single Carreau shear-thinning
  σ = σ_y + σ_y·(γ̇/γ̇_c)^½ + η₀·γ̇·[1+(λ·γ̇)²]^(-½)

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "tc_carreau"
PARAMS = ['sigma_y', 'gamma_dot_c', 'eta_0', 'lambda_val']
SCORECARD_PARAMS = ['sigma_y', 'eta_0']
LOG_PARAMS = ('sigma_y', 'gamma_dot_c', 'eta_0', 'lambda_val')
BOUNDS = {
    "sigma_y": (1e-12, np.inf),
    "gamma_dot_c": (1e-06, np.inf),
    "eta_0": (1e-12, np.inf),
    "lambda_val": (1e-12, np.inf),
}
# lambda -> 0 turns the Carreau term into eta_bg * gamma_dot
PARENT = 'tc'
PARENT_EXACT = True
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
    "eta_0": {"symbol": "η₀", "unit": "Pa·s", "description": "Zero-shear viscosity"},
    "lambda_val": {"symbol": "λ", "unit": "s", "description": "Characteristic relaxation time"},
}

def equation(gamma_dot, sigma_y, gamma_dot_c, eta_0, lambda_val):
    tc = sigma_y + sigma_y * np.sqrt(gamma_dot / gamma_dot_c)
    carreau = eta_0 * gamma_dot * (1.0 + (lambda_val * gamma_dot) ** 2) ** (-0.5)
    return tc + carreau

def get_equation_latex() -> str:
    return "σ = σ_y + σ_y·(γ̇/γ̇_c)^½ + η₀·γ̇·[1+(λ·γ̇)²]^(-½)"
