import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def compare_metrics(actual, predictions_dict, model_names=None):
    """
    Calculates RMSE for multiple models.
    
    Args:
        actual (pd.Series): The ground truth (test set).
        predictions_dict (dict): Key=Model Name, Value=Predicted Series/Array.
    
    Returns:
        pd.DataFrame: A table comparing metrics for all models.
    """
    results = {}
    
    for name, preds in predictions_dict.items():
        # Calculate RMSE
        rmse = np.sqrt(mean_squared_error(actual, preds))
        
        results[name] = {'RMSE': rmse}
    
    # Create DataFrame and sort by RMSE
    df_metrics = pd.DataFrame.from_dict(results, orient='index')
    return print(df_metrics.sort_values(by='RMSE'))

def plot_forecasts(test, predictions_dict, train=None, title="Forecast Comparison", xlabel="Date", ylabel="Industrial Production"):
    """
    Flexible plotting for N models, with or without training history.
    
    Args:
        test (pd.Series): The actual test data.
        predictions_dict (dict): Key=Model Name, Value=Predicted Series/Array.
        train (pd.Series, optional): If provided, plots historical context. If None, focuses on Test period.
        title (str): Plot title.
    """
    plt.figure(figsize=(14, 7))
    
    # 1. Plot Training Data (Optional)
    if train is not None:
        plt.plot(train.index, train, label='Training Data', color='gray', alpha=0.5)
        
    # 2. Plot Actual Test Data
    plt.plot(test.index, test, label='Actual Test', color='black', linewidth=2.5)
    
    # 3. Plot All Forecasts
    # Define a color cycle or line styles if you have many models
    styles = ['--', '-.', ':'] 
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'] # Matplotlib defaults
    
    for i, (name, preds) in enumerate(predictions_dict.items()):
        # Align index if prediction is a numpy array
        if not isinstance(preds, (pd.Series, pd.DataFrame)):
            preds = pd.Series(preds, index=test.index)
            
        style = styles[i % len(styles)]
        color = colors[i % len(colors)]
        
        plt.plot(preds.index, preds, label=f'{name} (Forecast)', linestyle=style, color=color, linewidth=2)

    plt.title(title, fontsize=14)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.show()