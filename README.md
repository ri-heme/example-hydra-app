# 🧪 Example Hydra App

This repo hosts an example Hydra app.

## Usage

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
NeuralNetwork(num_hidden=[200, 200], num_latent=40, dropout=0.2, lr=0.0001)
```
