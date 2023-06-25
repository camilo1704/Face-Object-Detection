import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from os.path import join
sns.set()

#def plot_results
results_path = "./results/results.csv"
save_path = "./results"
df = pd.read_csv(results_path)

fig, axes = plt.subplots( 3, 1,figsize=(8, 20), sharey=True)
sns.lineplot(ax=axes[0], x='epoch', y='loss', hue='Set', 
             data=pd.melt(df[["epoch","train/box_loss","val/box_loss"]], ['epoch'], value_name="loss", var_name="Set"))
axes[0].set_title("box_loss", weight="bold", fontsize=14)
sns.lineplot(ax=axes[1], x='epoch', y='loss', hue='Set', 
             data=pd.melt(df[["epoch","train/cls_loss","val/cls_loss"]], ['epoch'], value_name="loss", var_name="Set"))
axes[1].set_title("cls_loss", weight="bold", fontsize=14)
sns.lineplot(ax=axes[2], x='epoch', y='loss', hue='Set', 
             data=pd.melt(df[["epoch","train/dfl_loss","val/dfl_loss"]], ['epoch'], value_name="loss", var_name="Set"))
axes[2].set_title("dfl_loss", weight="bold", fontsize=14)
plt.savefig(join(save_path, "losses.png"))

fig, axes = plt.subplots( 2, 2,figsize=(10,12), sharey=True)
sns.lineplot(ax=axes[0, 0], data=df, x='epoch', y='metrics/precision(B)')
axes[0,0 ].set_title("precision", weight="bold", fontsize=14)
sns.lineplot(ax=axes[0, 1], data=df, x='epoch', y='metrics/recall(B)')
axes[0,1].set_title("recall", weight="bold", fontsize=14)
sns.lineplot(ax=axes[1,0], data=df, x='epoch', y='metrics/mAP50(B)')
axes[1,0].set_title("mAP50", weight="bold", fontsize=14)
sns.lineplot(ax=axes[1,1], data=df, x='epoch', y='metrics/mAP50-95(B)')
axes[1,1].set_title("mAP50-95", weight="bold", fontsize=14)
plt.savefig(join(save_path, "metrics.png"))