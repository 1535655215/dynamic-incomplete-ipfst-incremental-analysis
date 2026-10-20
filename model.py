"""Self-contained AP1 numerical reference implementation."""
from __future__ import annotations
import numpy as np

def phi(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=float)
    mu, nu = a[..., 0], a[..., 1]
    direction = np.where((mu == 0) & (nu == 0), .5,
                         1 - 2 / np.pi * np.arctan2(nu, mu))
    return np.stack([mu * mu, nu * nu, mu * mu + nu * nu, direction], axis=-1)

def full_ap1(a: np.ndarray):
    a = np.asarray(a, dtype=float)
    pairs = np.triu_indices(a.shape[0], 1)
    f = phi(a)
    d = np.sqrt(((f[pairs[0]] - f[pairs[1]]) ** 2).sum(axis=-1) / 3)
    colsum = d.sum(axis=0)
    weights = colsum / colsum.sum() if colsum.sum() else np.full(a.shape[1], 1/a.shape[1])
    conflict = (d * weights).sum(axis=1)
    return pairs, d, colsum, weights, conflict

def generate_table(n: int, m: int, seed: int = 20261020) -> np.ndarray:
    rng = np.random.default_rng(seed)
    u = rng.random((n, m))
    theta = rng.random((n, m)) * np.pi / 2
    return np.stack([np.sqrt(u) * np.cos(theta),
                     np.sqrt(u) * np.sin(theta)], axis=-1)
