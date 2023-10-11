# -*- coding: utf-8 -*-
"""
Module for rheology data fitting
--------------------------------

Provides functions for rheology models
Currently focusing on flowcurve

"""

def Newtonian(x, eta=0.1):
    """Newtonian model

    Note:

    .. math::
       \sigma=\eta\cdot\dot\gamma

    Args:

        eta : viscosity [Pa s]

    Returns:
        stress : Shear Stress, [Pa]
    """
    return eta * x


def Powerlaw(x, n=0.5, K=0.1):
    """Powerlaw model for the stress data

    Note:

    .. math::
       \sigma=K \cdot \dot\gamma^n

    Args:

        K : consistency index [Pa s]
        n : shear thinning index (1 for Newtonian) []

    Returns:
        stress : Shear Stress, [Pa]
    """
    return K * x ** n


def Bingham(x, ystress=1.0, eta_bg=0.1):
    """Bingham model

    Note:

    .. math::
       \sigma=\sigma_y+\eta_{bg}\cdot\dot\gamma

    Args:
        ystress: yield stress [Pa]

        eta_bg : Background viscosity [Pa s]

    Returns:
        stress : Shear Stress, [Pa]
    """
    return ystress + eta_bg * x


def TC(x, ystress=1.0, eta_bg=0.1, gammadot_crit=0.1):
    """Three component model

    Note:

    .. math::
       \sigma=\sigma_y+\sigma_y\cdot(\dot\gamma/\dot\gamma_c)^{0.5}+\eta_{bg}\cdot\dot\gamma

    Args:
        ystress: yield stress [Pa]

        eta_bg : Background viscosity [Pa s]

        gammadot_crit : Critical shear rate [1/s]

    Returns:
        stress : Shear Stress, [Pa]
    """
    return ystress + ystress * (x / gammadot_crit) ** 0.5 + eta_bg * x


def HB(x, ystress=1.0, K=1.0, n=0.5):
    """Hershel-Bulkley Model

    Note:

    .. math::
       \sigma= \sigma_y + K \cdot \dot\gamma^n

    Args:
        ystress: yield stress [Pa]

        K : Consistency index [Pa s^n]

        n : Shear thinning index []

    Returns:
        stress : Shear Stress, [Pa]
    """
    return ystress + K * x ** n

def casson(x, ystress=1.0, eta_bg=0.1):
    """Casson Model

    Note:

    .. math::
       \sigma^{0.5}= \sigma_y^{0.5} + \eta_{bg}^{0.5}

    Args:
        ystress: yield stress [Pa]

        eta_bg : Background viscosity [Pa s]

    Returns:
        stress : Shear Stress, [Pa]
    """
    return (ystress ** 0.5 + (eta_bg * x) ** 0.5) ** 2

def carreau(x, eta_0=1.0, gammadot_crit=1.0, n=0.5, prefix="carreau"):
    """carreau Model

    Note:

    .. math::
       \sigma=\dot\gamma \cdot \eta_0 \cdot (1+(\dot\gamma/\dot\gamma_c)^2)^{(n-1)/2}

    Args:
        eta_0: low shear viscosity [Pa s]

        gammadot_crit: critical shear rate [1/s]

        n : shear thinning exponent

    Returns:
        stress : Shear Stress, [Pa]
    """
    return x * eta_0 * (1 + (x / gammadot_crit) ** 2) ** ((n - 1) / 2)

def carreau(x, eta_0=1.0, gammadot_crit=1.0, n=0.5, prefix="carreau"):
    """carreau Model

    Note:

    .. math::
       \sigma=\dot\gamma \cdot \eta_0 \cdot (1+(\dot\gamma/\dot\gamma_c)^2)^{(n-1)/2}

    Args:
        eta_0: low shear viscosity [Pa s]
        gammadot_crit: critical shear rate [1/s]
        n : shear thinning exponent

    Returns:
        stress : Shear Stress, [Pa]
    """
    return x * eta_0 * (1 + (x / gammadot_crit) ** 2) ** ((n - 1) / 2)


def carreau_yasuda(x, mu_0, mu_inf, lambda_1, n):
    """Calculates the viscosity of a non-Newtonian fluid using the Carreau-Yasuda model.

    .. math::
        \sigma  = \eta(\mu_{\infty} + (\mu_0 - \mu_{\infty}) \left( 1 + (\lambda_1 \dot\gamma)^2 \right)^{(n - 1)/2})

    Args:
        x: The shear rate in 1/s.
        mu_0: The zero-shear viscosity in Pa*s.
        mu_inf: The infinite-shear viscosity in Pa*s.
        lambda_1: The relaxation time in s.
        n: The power-law index.

    Returns:
        stress : Shear Stress, [Pa]
    """

    return x*(mu_inf + (mu_0 - mu_inf) * (1 + (lambda_1 * x)**2)**((n - 1) / 2))


def cross(x, eta_inf=0.001, eta_0=1.0, n=0.5, gammadot_crit=1.0):
    """cross Model

    Note:

    .. math::
       \sigma= \dot\gamma \eta_{inf} + \dot\gamma (\eta_0 - \eta_{inf})/(1 + (\dot\gamma/\dot\gamma_c)^n)

    Args:
        ystress: yield stress [Pa]

        K : Consistency index [Pa s^n]

        n : Shear thinning index []

    Returns:
        stress : Shear Stress, [Pa]
    """
    return x * eta_inf + x * (eta_0 - eta_inf) / (1 + (x / gammadot_crit) ** n)


model_dict={
    'caggioni2020variations':TC, 
    'herschel_bulkley_1926':HB,
    'newton_1687':Newtonian, 
    'ostwald_1929':Powerlaw, 
    'carreau_yasuda_1979':carreau,
    'cross_1925':cross,
    'bingham_1916':Bingham,
}

bib_file='models.bib'