import hydra
from hydra.core.hydra_config import HydraConfig
from hydra.types import RunMode

from hydra_app.conf import AppConfig


@hydra.main(config_path="conf", config_name="main")
def main(config: AppConfig) -> None:
    hydra_config = HydraConfig.get()
    if hydra_config.mode != RunMode.MULTIRUN:
        raise ValueError("Must run on multirun mode.")
    net = hydra.utils.instantiate(config.model)
    print(
        f"Hydra job #{hydra_config.job.num + 1} ({hydra_config.job.override_dirname})"
    )
    print(f"Model: {net}\nTraining epochs: {config.training.num_epochs}")


if __name__ == "__main__":
    main()
