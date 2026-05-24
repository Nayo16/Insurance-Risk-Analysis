import matplotlib.pyplot as plt
import seaborn as sns


def plot_loss_ratio_by_group(df, group_col, value_col="LossRatio"):
    plt.figure(figsize=(10,6))
    agg = df.groupby(group_col)[value_col].mean().sort_values(ascending=False)
    sns.barplot(x=agg.values, y=agg.index)
    plt.xlabel(value_col)
    plt.title(f"Average {value_col} by {group_col}")
    plt.tight_layout()
    return plt.gcf()
