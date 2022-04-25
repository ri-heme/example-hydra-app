__all__ = ["create_model"]

from dataclasses import dataclass
from pathlib import Path

import hydra


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
    config_path = Path(__file__).parents[1] / "conf"
    with hydra.initialize_config_dir(config_path.as_posix()):
        config = hydra.compose("main")
        return hydra.utils.instantiate(config.model)
