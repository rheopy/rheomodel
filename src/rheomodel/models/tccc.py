"""
TCCC — Three-Component Carreau-Carreau
  σ = σ_y + σ_y·(γ̇/γ̇_c)^½ + η₀,₁·γ̇·[1+(λ₁·γ̇)²]^(-¼) + η₀,₂·γ̇·[1+(λ₂·γ̇)²]^(-½)

Pure science: equation, parameters, citations.
Fitting machinery (initial guesses, ladder seeding, robust_fit) lives in rheofit.
"""
import numpy as np

MODEL_NAME = "tccc"
PARAMS = ['sigma_y', 'gamma_dot_c', 'eta_0_1', 'lambda_val_1', 'eta_0_2', 'lambda_val_2']
SCORECARD_PARAMS = ['sigma_y', 'eta_0_1', 'eta_0_2']
LOG_PARAMS = ('sigma_y', 'gamma_dot_c', 'eta_0_1', 'lambda_val_1', 'eta_0_2', 'lambda_val_2')
BOUNDS = {
    "sigma_y": (1e-12, np.inf),
    "gamma_dot_c": (1e-06, np.inf),
    "eta_0_1": (1e-12, np.inf),
    "lambda_val_1": (1e-12, np.inf),
    "eta_0_2": (1e-12, np.inf),
    "lambda_val_2": (1e-12, np.inf),
}
# eta_0_1 -> 0 recovers TC-Carreau
PARENT = 'tc_carreau'
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
    "eta_0_1": {"symbol": "η₀,₁", "unit": "Pa·s", "description": "Zero-shear viscosity, first Carreau mode"},
    "lambda_val_1": {"symbol": "λ₁", "unit": "s", "description": "Relaxation time, first Carreau mode"},
    "eta_0_2": {"symbol": "η₀,₂", "unit": "Pa·s", "description": "Zero-shear viscosity, second Carreau mode"},
    "lambda_val_2": {"symbol": "λ₂", "unit": "s", "description": "Relaxation time, second Carreau mode"},
}

def equation(gamma_dot, sigma_y, gamma_dot_c, eta_0_1, lambda_val_1, eta_0_2, lambda_val_2):
    tc = sigma_y + sigma_y * np.sqrt(gamma_dot / gamma_dot_c)
    c1 = eta_0_1 * gamma_dot * (1.0 + (lambda_val_1 * gamma_dot) ** 2) ** (-0.25)
    c2 = eta_0_2 * gamma_dot * (1.0 + (lambda_val_2 * gamma_dot) ** 2) ** (-0.5)
    return tc + c1 + c2

def get_equation_latex() -> str:
    return "σ = σ_y + σ_y·(γ̇/γ̇_c)^½ + η₀,₁·γ̇·[1+(λ₁·γ̇)²]^(-¼) + η₀,₂·γ̇·[1+(λ₂·γ̇)²]^(-½)"
