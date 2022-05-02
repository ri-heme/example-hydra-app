import hydra

from hydra_app.conf import AppConfig


@hydra.main(config_path="conf", config_name="main")
def main(config: AppConfig) -> None:
    net = hydra.utils.instantiate(config.model)
    print(str(net))


if __name__ == "__main__":
    main()
