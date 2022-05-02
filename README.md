# 🧪 Example Hydra App

This repo hosts an example Hydra app.

## Usage

### In a Notebook

Create a model in a Notebook or another script by calling `create_model`.

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

Create an `my_conf/experiment` folder and place inside a config file (in the
example below it's called `test.yaml`). Then, from the command line, call the
app, specify the name of the config file without extension as `experiment=test`
and the path to the folder using the `-cd` argument.

```python
>>> python hydra_app experiment=test -cd myconf
NeuralNetwork(num_hidden=[200, 200], num_latent=16, dropout=0.0, lr=0.1)
```
