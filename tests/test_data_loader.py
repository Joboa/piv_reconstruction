"""
Unit tests for LESDataLoader class.
"""

import pytest
from pathlib import Path
from backend.data_loader import LESDataLoader

def test_init_creates_loader():
    """Test that LESDataLoader can be instantiated."""

    loader = LESDataLoader('data/raw/gap_025', 0.25)

    assert loader.gap_ratio == 0.25
    # assert loader.data_path == Path('data/raw/gap_0.25')
    assert loader.u_field is None
    assert loader.v_field is None
    assert loader.n_snapshots is None