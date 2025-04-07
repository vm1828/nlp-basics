from collections import OrderedDict
import os
from dataclasses import dataclass
import torch


@dataclass
class Hyperparameters:
    epochs: int
    lr: float
    batch_size: int


@dataclass
class HyperparametersSkipGram(Hyperparameters):
    emb_dim: int
    vocab_size: int


@dataclass
class SavedModel:
    model_state_dict: OrderedDict
    model_hyperparameters: dict

    def save_model(self, model_name: str) -> None:
        """Save the model state and hyperparameters to a file."""
        path = os.path.join('models', f'{model_name}.pth')
        if os.path.exists(path):
            confirmation = input(
                f"The model {path} already exists. Do you want to overwrite it? (y/n): ").strip().lower()

            if confirmation != 'y':
                new_name = input('Enter new name for this model:')
                path = os.path.join('models', f'{new_name}.pth')

        torch.save(self, path)
        print(f'Model saved to {path}')


@dataclass
class SavedModelSkipGram(SavedModel):
    model_hyperparameters: HyperparametersSkipGram
