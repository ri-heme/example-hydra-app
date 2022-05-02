__all__ = ["AppConfig"]

from dataclasses import dataclass, field

from hydra.core.config_store import ConfigStore

from hydra_app.model.network import NeuralNetwork


@dataclass
class ModelConfig:
    _target_: str = NeuralNetwork.__name__
    lr: float = 0.0001
    num_hidden: list[int] = field(default_factory=lambda: [200, 200])
    num_latent: int = 20
    dropout = 0.2


@dataclass
class TrainingConfig:
    num_epochs: int = 200


@dataclass
class AppConfig:
    model: ModelConfig = ModelConfig()
    training: TrainingConfig = TrainingConfig()
    name: str = "Test"
    seed: int = 123456


cs = ConfigStore.instance()
cs.store(name="config", node=AppConfig)
