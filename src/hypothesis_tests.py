import scipy.stats as stats
import pandas as pd


def chi2_test_categorical(df: pd.DataFrame, col, target_col="HasClaim"):
    """Perform chi-squared test between categorical column and binary target."""
    ct = pd.crosstab(df[col], df[target_col])
    chi2, p, dof, ex = stats.chi2_contingency(ct)
    return dict(chi2=chi2, p_value=p, dof=dof)


def ttest_group_mean(df: pd.DataFrame, group_col, value_col):
    """Two-sample t-test between group and rest (for simplicity)."""
    groups = df[group_col].unique()
    results = {}
    overall = df[value_col].dropna()
    for g in groups:
        a = df[df[group_col]==g][value_col].dropna()
        b = overall[~df[group_col].isin([g])]
        tstat, p = stats.ttest_ind(a, b, equal_var=False, nan_policy='omit')
        results[g] = dict(tstat=float(tstat), p_value=float(p))
    return results
