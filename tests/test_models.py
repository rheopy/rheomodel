"""Tests for rheomodel: equations, ladder, registry, citations."""

import re

import numpy as np
import pytest

import rheomodel
from rheomodel import get_model, list_models
from rheomodel.models import MODELS


def test_registry_has_nine_models():
    assert list_models() == sorted(MODELS)
    assert len(MODELS) == 9


def test_get_model_unknown_raises():
    with pytest.raises(KeyError):
        get_model("not_a_model")


def test_metadata_consistent():
    for name, m in MODELS.items():
        assert m.MODEL_NAME == name
        assert set(m.BOUNDS) == set(m.PARAMS)
        assert set(m.LOG_PARAMS) <= set(m.PARAMS)
        assert set(m.SCORECARD_PARAMS) <= set(m.PARAMS)
        assert set(m.PARAM_INFO) == set(m.PARAMS)
        assert m.get_equation_latex().strip()
        for lo, hi in m.BOUNDS.values():
            assert lo < hi


def test_equation_spot_values():
    x = np.array([1.0])
    assert get_model("bingham").equation(x, sigma_y=10.0, K=2.0)[0] == pytest.approx(12.0)
    assert get_model("herschel_bulkley").equation(x, sigma_y=10.0, K=2.0, n=0.5)[0] == pytest.approx(12.0)
    assert get_model("power_law").equation(x, K=3.0, n=2.0)[0] == pytest.approx(3.0)
    # Casson: (sqrt(9) + sqrt(4*1))^2 = 25
    assert get_model("casson").equation(x, sigma_y=9.0, K=4.0)[0] == pytest.approx(25.0)
    # Carreau at x -> 0 tends to eta_0 * x
    c = get_model("carreau").equation(np.array([1e-9]), eta_0=5.0, lambda_val=1.0, n=0.5)[0]
    assert c == pytest.approx(5e-9, rel=1e-6)


def test_exact_nesting_hb_to_bingham():
    x = np.logspace(-2, 2, 20)
    hb = get_model("herschel_bulkley").equation(x, sigma_y=7.0, K=3.0, n=1.0)
    bi = get_model("bingham").equation(x, sigma_y=7.0, K=3.0)
    assert np.allclose(hb, bi, rtol=1e-12)


def test_exact_nesting_tc_carreau_to_tc():
    x = np.logspace(-2, 2, 20)
    tcc = get_model("tc_carreau").equation(x, sigma_y=7.0, gamma_dot_c=0.5, eta_0=2.0, lambda_val=1e-9)
    tc = get_model("tc").equation(x, sigma_y=7.0, gamma_dot_c=0.5, eta_bg=2.0)
    assert np.allclose(tcc, tc, rtol=1e-6)


def test_exact_nesting_tccc_to_tc_carreau():
    x = np.logspace(-2, 2, 20)
    t3 = get_model("tccc").equation(
        x, sigma_y=7.0, gamma_dot_c=0.5,
        eta_0_1=1e-12, lambda_val_1=0.3, eta_0_2=2.0, lambda_val_2=1.0)
    tcc = get_model("tc_carreau").equation(
        x, sigma_y=7.0, gamma_dot_c=0.5, eta_0=2.0, lambda_val=1.0)
    assert np.allclose(t3, tcc, rtol=1e-6)


def test_ladder_flags():
    assert get_model("herschel_bulkley").PARENT == "bingham"
    assert get_model("herschel_bulkley").PARENT_EXACT is True
    assert get_model("carreau_carreau").PARENT_EXACT is False  # advisory only
    assert get_model("bingham").PARENT is None


def test_citations_have_valid_doi_shape():
    pat = re.compile(r"^10\.\d{4,}/.+")
    for name, m in MODELS.items():
        doi = m.CITATION["doi"]
        assert m.CITATION["authors"] and m.CITATION["year"] and m.CITATION["title"]
        if doi is not None:
            assert pat.match(doi), (name, doi)


def test_known_citation_fixes():
    # 2026-10-02: these DOIs were wrong in the rheofit docs; must stay fixed.
    assert get_model("tc").CITATION["doi"] == "10.1122/1.5120633"
    assert get_model("tc_carreau").CITATION["doi"] == "10.1122/1.5120633"
    assert get_model("tccc").CITATION["doi"] == "10.1122/1.5120633"
    assert "elastoplastic transition" not in get_model("tc_carreau").CITATION["title"].lower()
