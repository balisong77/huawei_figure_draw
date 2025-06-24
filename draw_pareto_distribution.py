from common import *
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os, sys

style = get_style_sheet_upon_base("motivation-throughput.mplstyle")

pareto_df = pd.read_csv(os.path.join("data", "pareto_ratio_5alpha.csv"))

# colors = ["#ADA0D8","#E8B05E", "#AAD490","#F8CEB2","#78ADDE", '#4169e1']
# colors = ['#165316','#2ca02c', '#35cc35']
colors = ['#66bf66','#46b046', '#2ca02c', '#228022', '#176617']
custom_palette = sns.color_palette(colors)

figsize = (14, 6)
tick_label_size = 18

# 吞吐柱状图
with plt.style.context(style):
    # 创建绘图
    fig, ax1 = plt.subplots(figsize=figsize)
    ax1.grid(False)
    ax1.tick_params(axis='x', labelsize=tick_label_size)
    
    # 绘制左边柱状图
    sns.barplot(x='protocol', y='count', data=pareto_df, hue='pareto', palette=custom_palette, ax=ax1, zorder=2, edgecolor='black', alpha=0.7)
    ax1.set_ylabel('Traffic Ratio')
    ax1.set_xlabel('Protocol')
    ax1.tick_params(axis='y')
    ax1.set_ylim(0, 3000)
    # for hues, hatch in zip(ax1.containers, hatches):
    #     # set a different hatch for each time
    #     for hue in hues:
    #         hue.set_hatch(hatch)
    # 问题：legend中不显示hetche
    # 解决方案：手动添加legend
    handles = [mpl.patches.Patch(edgecolor='black', facecolor=custom_palette[i], label=pareto_df['pareto'].unique()[i]) for i in range(len(custom_palette))]
    legend = ax1.legend(handles=handles, fontsize=18, loc='upper center', ncol=3)
    for i, handle in enumerate(legend.legend_handles):
        handle.set_facecolor(custom_palette[i])
    # 添加数据标签
    # for p in ax1.patches:
    #     height = p.get_height()
    #     if height > 0: 
    #         ax1.annotate("{:.0f}".format(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=14)
    
    # 显示图形
    # plt.savefig(os.path.join(FIGURE_DIR, "chap3_pareto_distribution.pdf"), format='pdf')
    plt.savefig(os.path.join("images", "dynamic_traffic_pareto_distribution.png"), format='png')
    plt.show()

