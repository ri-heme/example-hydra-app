import hydra
from omegaconf import OmegaConf

from hydra_app.conf import AppConfig


@hydra.main(config_path="conf", config_name="main")
def main(config: AppConfig) -> str:
    txt = OmegaConf.to_yaml(config)
    print(txt)
    return txt


if __name__ == "__main__":
    main()
