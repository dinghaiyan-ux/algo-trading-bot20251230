import pandas as pd

def calculate_sma(data, window):
    """
    Calculate Simple Moving Average (SMA).
    
    Args:
        data (pd.Series): The price data.
        window (int): The rolling window size.
        
    Returns:
        pd.Series: The SMA values.
    """
    return data.rolling(window=window).mean()

def strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    
    signals['short_mavg'] = calculate_sma(data['close'], short_window)
    signals['long_mavg'] = calculate_sma(data['close'], long_window)
    
    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    return signals

