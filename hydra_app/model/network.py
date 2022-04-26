__all__ = ["create_model"]

from dataclasses import dataclass

import hydra
from omegaconf import DictConfig, OmegaConf

import hydra_app.conf


@dataclass
class NeuralNetwork:
    """A neural network class."""

    num_hidden: list[int]
    num_latent: int
    dropout: float
    lr: float


def create_model(user_config: DictConfig) -> "NeuralNetwork":
    """Factory method. Returns a neural network object created using default
    and user configuration.
    """
    with hydra.initialize_config_module(hydra_app.conf.__name__):
        base_config = hydra.compose("main")
        if user_config is not None:
            config = OmegaConf.merge(base_config, user_config)
        else:
            config = base_config
        return hydra.utils.instantiate(config.model)
