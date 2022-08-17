__all__ = ["ExampleSearchPathPlugin"]

from pathlib import Path

from hydra.core.config_search_path import ConfigSearchPath
from hydra.plugins.search_path_plugin import SearchPathPlugin


class ExampleSearchPathPlugin(SearchPathPlugin):
    def manipulate_search_path(self, search_path: ConfigSearchPath) -> None:
        path = Path.cwd() / "config"
        path.mkdir(exist_ok=True)
        search_path.append("hydra_app", f"file://{path}")
