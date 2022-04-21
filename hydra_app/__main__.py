import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="conf", config_name="main")
def main(config: DictConfig) -> str:
    txt = OmegaConf.to_yaml(config)
    print(txt)
    return txt


if __name__ == "__main__":
    main()
