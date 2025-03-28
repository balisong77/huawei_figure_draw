from exp_common import *
import pandas as pd
import os 
import numpy as np
from common import *
import seaborn as sns

def add_suffix_all(value):
    return "%s-%s"%(value, "all")
def add_suffix_small(value):
    return "%s-%s"%(value, "small")

styles = get_style_sheet_upon_base("draw-baseline.mplstyle")

targets =  ["32", "48", "64", "96", "128", "192", "256", "BF", "BF_notimeout", "GA_real", "SGD_predict", "GA_sim"]

## data 
# 读取 CSV 文件

df = read_dfs_node35()

print(df)

filtered_df = df[df['tag'].isin(targets)]


print(filtered_df)


# 绘图
with plt.style.context(styles):   
    sns.set_context("paper", font_scale=2.5)
    fig, ax0 = plt.subplots(1, 1, figsize=(12, 6))

    
    sns.barplot(x='tag', y='throughput_mpps', data=filtered_df, ax=ax0, color=colors[2], alpha=0.9)
    
    ax1 = ax0.twinx()
    sns.lineplot(ax = ax1,
                data = filtered_df,
                x = 'tag',
                y = 'timeout_rate_100',
                marker = linemarker[0],
                markersize= g_marker_size,
                #  errorbar=('ci', 95),
                linewidth=g_linewidth,
                color = colors[0])
    
    for i, line in enumerate(ax1.lines):
        plt.setp(line, linestyle=linestyle[i % len(linestyle)])
        line.set_markeredgecolor(colors[0])
        line.set_markerfacecolor("none")
        line.set_markeredgewidth(2)
    for p in ax0.patches:
        ax0.text(
            p.get_x() + p.get_width() / 2,  # x 坐标：柱子中心
            p.get_height() + 0.04,           # y 坐标：柱子高度 + 偏移量
            f'{p.get_height():.2f}',        # 显示的文本（数值）
            ha='center',                    # 水平对齐方式
            va='bottom',                    # 垂直对齐方式
            fontsize=12                     # 字体大小
        )
    line = ax1.lines[0]  # seaborn 的 lineplot 会返回一个线条对象

    # 获取线条的数据点
    x_data = line.get_xdata()  # 获取 x 数据
    y_data = line.get_ydata()  
    for x_val, y_val in zip(x_data, y_data):
        ax0.text(
            x_val,                  # x 坐标
            y_val + 0.1,              # y 坐标 + 偏移量
            f'{y_val:.3f}',         # 显示的文本（数值）
            ha='center',            # 水平对齐方式
            va='bottom',            # 垂直对齐方式
            fontsize=12,            # 字体大小
            color='blue'            # 字体颜色
        )
    
    ax0.patches[-1].set_color(colors[1])
    
    ax0.set_xlabel("")
    ax0.set_ylabel("Throughput (mpps)")
    ax1.set_ylabel("Timeout rate (%)")
    ax0.set_ylim(0, 5)
    ax1.set_ylim(0, 5)
    
    #ax0.legend(loc='upper center', labels = ["distribution1", "distribution2", "distribution3"], ncols=3)
           
    #控制上下图的间隔
    plt.subplots_adjust(hspace=0.3)

    ax0.tick_params(axis='x', rotation=30)
    ax0.tick_params(axis='y')
    ax0.set_xticks(targets)
    # ax0.set_title(titles[i], fontsize=24)  # 为每个子图设置标题
    
    # 设置marker style
    
    # 显示图表
    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    fig.tight_layout()
    save_figure('GASim35')
    # plt.show()