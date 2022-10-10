# 🧪 Example Hydra App

This repo hosts an example Hydra app.

## Usage

### In a Notebook

Create a model in a Notebook or another script by calling `create_model`. This
is a custom function that reads the default configuration and returns an 
initialized class instance.

```python
>>> from hydra_app import create_model
>>> 
>>> net = create_model()
>>> print(net)
NeuralNetwork(num_hidden=[200, 200], num_latent=20, dropout=0.2, lr=0.0001)
```

Override base configuration by supplying an additional config.

```python
>>> from omegaconf import OmegaConf
>>> 
>>> experiment_conf = OmegaConf.load("experiment.yaml")
>>> 
>>> net = create_model(experiment_conf)
>>> print(net)
NeuralNetwork(num_hidden=[200, 200], num_latent=16, dropout=0.0, lr=0.1)
```

### From the command line

Run:

```bash
>>> python -m hydra_app
NeuralNetwork(num_hidden=[200, 200], num_latent=20, dropout=0.2, lr=0.0001)
```

The above command uses the default configuration. To override it, you can check 
the default options using `--help`:

```bash
>>> python -m hydra_app --help
```

For example, load the "other" model which is specified in 
[`conf/model/other.yaml`](hydra_app/conf/model/other.yaml).

```bash
>>> python -m hydra_app model=other
NeuralNetwork(num_hidden=[100, 100], num_latent=10, dropout=0.1, lr=0.0003)
```

#### Reading additional config files

You can also read an additional file that overrides the default configuration.

The app will automatically create a `config` folder in the current working 
directory. Create an `experiment` sub-folder and place inside a config file 
(such  as [`test.yaml`](config/experiment/test.yaml)). See below the 
directory structure:


```
.
└── config/
    └── experiment/
        └── test.yaml
```

Then, from the command line, call the app specifying the name of the config
file (without extension):

```bash
>>> python -m hydra_app +experiment=test
NeuralNetwork(num_hidden=[100, 100], num_latent=10, dropout=0.1, lr=0.1)
```

Note that you can extend the available config options by reproducing the 
configuration structure inside the `config` folder in your current working 
directory. For example, adding a `model` folder with some model YAMLs:

```
.
└── config/
    ├── model/
    │   ├── network1.yaml
    │   └── network2.yaml
    └── experiment/
        └── test.yaml
```

will make it possible to select those model configs:

```bash
>>> python -m hydra_app model=network2 --help
```

## Multirun

If we want to run a job multiple times, we can run the application with `-m` 
(or `--multirun`):

```bash
>>> python -m hydra_app -m model=other,another
NeuralNetwork(num_hidden=[100, 100], num_latent=10, dropout=0.1, lr=0.0003)
NeuralNetwork(num_hidden=[100, 100, 20], num_latent=2, dropout=0.1, lr=0.5)
```

Alternatively, we can force the multirun mode on the Hydra config (see
[`multirun.yaml`](config/experiment/multirun.yaml)).

```bash
>>> python -m hydra_app +experiment=multirun
NeuralNetwork(num_hidden=[200, 200], num_latent=20, dropout=0.2, lr=0.1)
NeuralNetwork(num_hidden=[200, 200], num_latent=20, dropout=0.2, lr=0.1)
NeuralNetwork(num_hidden=[100, 100], num_latent=10, dropout=0.1, lr=0.1)
NeuralNetwork(num_hidden=[100, 100], num_latent=10, dropout=0.1, lr=0.1)
NeuralNetwork(num_hidden=[100, 100, 20], num_latent=2, dropout=0.1, lr=0.1)
NeuralNetwork(num_hidden=[100, 100, 20], num_latent=2, dropout=0.1, lr=0.1)
```

Finally, we can access the job number and mode from the `HydraConfig` object.
This can be useful to report the current job, or to make sure that a certain 
task runs on a specific mode.

```python
from hydra.core.hydra_config import HydraConfig
from hydra.types import RunMode

@hydra.main(config_path="conf", config_name="main")
def main(config: AppConfig) -> None:
    hydra_config = HydraConfig.get()
    if hydra_config.mode != RunMode.MULTIRUN:
        raise ValueError("Must run on multirun mode.")
    print(f"Hydra job #{hydra_config.job.num + 1}")
```
