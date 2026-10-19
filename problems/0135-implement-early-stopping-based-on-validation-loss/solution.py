from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    # Your code here
    if not val_losses:
        raise ValueError("val_losses cannot be empty")
    
    best_loss = float("inf")
    best_epochs = 0
    epochs_without_improvement=0

    for epochs, loss in enumerate(val_losses):

        if loss<best_loss-min_delta:
            best_loss=loss
            best_epochs = epochs
            epochs_without_improvement =0
        else:
            epochs_without_improvement+=1

        if epochs_without_improvement>=patience:
            return epochs,best_epochs

    return len(val_losses)-1,best_epochs