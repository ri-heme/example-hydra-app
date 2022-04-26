__version__ = "0.1.0"
__author__ = "Ricardo Hernández Medina <ricardo.medina@cpr.ku.dk>"
__all__ = ["conf", "create_model"]

from hydra_app import conf
from hydra_app.model.network import create_model
