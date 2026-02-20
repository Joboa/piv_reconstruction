"""
Data loader for LES velocity field data.
Handles loading and basic operations on PIV/LES datasets.
"""

import numpy as np
from pathlib import Path


class LESDataLoader:
    """
    Load and manage LES velocity field data.

    Attributes:
        data_path (Path): Path to data directory
        u_field (np.ndarray): U velocity component, shape (N, H, W)
        v_field (np.ndarray): V velocity component, shape (N, H, W)
        x_coords (np.ndarray): X coordinates, shape (H, W)
        y_coords (np.ndarray): Y coordinates, shape (H, W)
        gap_ratio (float): Gap to diameter ratio (0.25 or 0.50)
    """

    def __init__(self, data_path, gap_ratio):
        """
        Initialize the data loader.

        Args:
            data_path (str or Path): Path to directory containing .npy files
        """
        self.data_path = Path(data_path)
        self.gap_ratio = gap_ratio

        self.u_field = None
        self.v_field = None
        self.x_coords = None
        self.y_coords = None

        # Metadata
        self.n_snapshots = None
        self.height = None
        self.width = None
