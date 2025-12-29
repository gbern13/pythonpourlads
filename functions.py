import statsmodels.api as sm
import pandas as pd

def wls_model(df, target, weight_col, drop_cols=None, cov_type='HC1'):
    """
    df : pandas DataFrame
    target : string
    weight_col : string
    drop_cols : list of strings
    cov_type : string
    """
    if drop_cols is None:
        drop_cols = []
    
    to_drop = [target, weight_col] + drop_cols
    
    if 'CNTSTUID' in df.columns:# on enlève CNTSTUID et id si ils existent
        to_drop.append('CNTSTUID')
    if 'id' in df.columns:
        to_drop.append('id')
        
    to_drop = list(set([c for c in to_drop if c in df.columns]))
    
    X = df.drop(columns=to_drop)
    y = df[target]
    weights = df[weight_col]
    
    X_const = sm.add_constant(X)
    
    model = sm.WLS(y, X_const, weights=weights).fit(cov_type=cov_type)
    return model

def ols_model(df, target,drop_cols=None, cov_type='HC1'):
    """
    df : pandas DataFrame
    target : string
    drop_cols : list of strings
    cov_type : string
    """
    if drop_cols is None:
        drop_cols = []
    
    to_drop = [target] + drop_cols
    
    if 'CNTSTUID' in df.columns:# on enlève CNTSTUID et id si ils existent
        to_drop.append('CNTSTUID')
    if 'id' in df.columns:
        to_drop.append('id')
        
    to_drop = list(set([c for c in to_drop if c in df.columns]))
    
    X = df.drop(columns=to_drop)
    y = df[target]
    
    X_const = sm.add_constant(X)
    
    model = sm.OLS(y, X_const).fit(cov_type=cov_type)
    return model