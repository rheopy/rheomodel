# -*- coding: utf-8 -*-
"""
Module for rheology data fitting
--------------------------------

Provides functions for rheology models
Currently focusing on flowcurve

"""

def latex_repr(r):
    def wrapper(f):
        f.latex = r
        return f
    return wrapper


@latex_repr(r'$\sigma=\eta\cdot\dot\gamma$')
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

@latex_repr(r'$\sigma=K \cdot \dot\gamma^n$')
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

@latex_repr(r'$\sigma=\sigma_y+\eta_{bg}\cdot\dot\gamma$')
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

@latex_repr(r'$\sigma=\sigma_y+\sigma_y\cdot(\dot\gamma/\dot\gamma_c)^{0.5}+\eta_{bg}\cdot\dot\gamma$')
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

@latex_repr(r'$\sigma= \sigma_y + K \cdot \dot\gamma^n$')
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

@latex_repr(r'$\sigma^{0.5}= \sigma_y^{0.5} + \eta_{bg}^{0.5}$')
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

@latex_repr(r'$\sigma=\dot\gamma \cdot \eta_0 \cdot (1+(\dot\gamma/\dot\gamma_c)^2)^{(n-1)/2}$')
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

@latex_repr(r'$\sigma= \dot\gamma \eta_{inf} + \dot\gamma (\eta_0 - \eta_{inf})/(1 + (\dot\gamma/\dot\gamma_c)^n)$')
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
    'cross_1925':cross,
    'bingham_1916':Bingham,
}

bib_file='models.bib'