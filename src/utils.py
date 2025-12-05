import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def compare_metrics(actual, predictions_dict, benchmark_name=None):
    """
    Calculates RMSE and MAE for multiple models. 
    Optionally calculates ratios against a benchmark if benchmark_name is provided.
    
    Returns:
        pd.DataFrame: A table containing the metrics.
    """
    results = {}
    
    # 1. Calculate Metrics
    for name, preds in predictions_dict.items():
        rmse = np.sqrt(mean_squared_error(actual, preds))
        mae = mean_absolute_error(actual, preds)
        results[name] = {'RMSE': rmse, 'MAE': mae}
    
    # 2. Create DataFrame
    df_metrics = pd.DataFrame.from_dict(results, orient='index')
    
    # 3. Optional: Add Ratios if a benchmark is provided and exists
    if benchmark_name and benchmark_name in df_metrics.index:
        rw_rmse = df_metrics.loc[benchmark_name, 'RMSE']
        rw_mae = df_metrics.loc[benchmark_name, 'MAE']
        
        df_metrics['RMSFE Ratio'] = df_metrics['RMSE'] / rw_rmse
        df_metrics['MAFE Ratio'] = df_metrics['MAE'] / rw_mae
        
    # 4. Return sorted DataFrame (Do not wrap in print!)
    return df_metrics.sort_values(by='RMSE')

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