__all__ = ["create_model"]

from dataclasses import dataclass
from pathlib import Path

import hydra

import hydra_app.conf

@dataclass
class NeuralNetwork:
    """A neural network class."""

    num_hidden: list[int]
    num_latent: int
    dropout: float
    lr: float


def create_model() -> "NeuralNetwork":
    """Factory method. Returns a neural network object created using default
    configuration.
    """
    with hydra.initialize_config_module(hydra_app.conf.__name__):
        config = hydra.compose("main")
        return hydra.utils.instantiate(config.model)
