from common import *
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os, sys

style = get_style_sheet_upon_base("motivation-throughput.mplstyle")

# 数据源
# rl_df = pd.read_csv(os.path.join(DATA_PATH, "huawei-dynamic-rl", "0605_dynamic_pareto.csv"))
# rl_df = pd.read_csv(os.path.join(DATA_PATH, "huawei-dynamic-rl", "0611_dynamic_protocol.csv"))
# rl_df = pd.read_csv(os.path.join(DATA_PATH, "huawei-dynamic-rl", "0614_dynamic_ratio.csv"))
# rl_df = pd.read_csv(os.path.join(DATA_PATH, "huawei-dynamic-rl", "0616_dynamic_ratio_cost.csv"))
# rl_df = pd.read_csv(os.path.join(DATA_PATH, "huawei-dynamic-rl", "0617_dynamic_ratio_protocolloss.csv"))
rl_df = pd.read_csv(os.path.join(DATA_PATH, "huawei-dynamic-rl", "0619_dynamic_ratio_moreaction.csv.csv"))

rl_df['throughput'] = rl_df['throughput'] / 1e6
rl_df['timeout_rate'] = rl_df['timeout_rate'] * 100
rl_df['tag'] = rl_df['tag'].apply(lambda x: x.replace('_fixed_all_', 'fix_').replace('_train_checkpoint_', 'train_'))

hatches = ['//', '\\', '/\\', '|', '-', '+', 'x', 'o', 'O', '.']
colors = ["#ADA0D8","#E8B05E", "#AAD490","#F8CEB2","#78ADDE", '#4169E1', '#FFA07A', '#949FB1', '#D20103', '#8DD3C7']
custom_palette = sns.color_palette(colors)
markers = ['o', 's', 'D', 'p', '^', 'h', 'X', 'd', '<', '>']

# 根据最优的智能体选择
# tags = ['fix_32', 'fix_64', 'fix_128', 'fix_192', 'fix_256', 'train_5000_steps', 'train_55000_steps', 'train_100000_steps']
tags = ['fix_32', 'fix_64', 'fix_128', 'fix_192', 'fix_256', 'train_50000_steps']

figsize = (12, 8)
tick_label_size = 18

# 吞吐折线图
with plt.style.context(style):
    # 创建绘图
    fig3, ax3 = plt.subplots(figsize=figsize)
    ax3.grid(False)
    ax3.tick_params(axis='x', labelsize=tick_label_size)
    for tag in tags:
        group = rl_df[rl_df['tag'] == tag]
        sns.lineplot(x='step', y='throughput', data=group, ax=ax3, zorder=2, marker=markers[tags.index(tag)], label=tag, color=custom_palette[tags.index(tag)])
    ax3.set_ylabel('Throughput (Mpps)')
    ax3.set_xlabel('Step')
    ax3.set_xticks(rl_df['step'].unique())

    ax3.tick_params(axis='y')
    # 调整Y轴范围
    # ax3.set_ylim(3.6, 4.6)
    for line in ax3.lines:
        line.set_linewidth(3)
        line.set_markersize(6)
    for marker in ax3.collections:
        marker.set_sizes([100])

    for hues, hatch in zip(ax3.containers, hatches):
        # set a different hatch for each time
        for hue in hues:
            hue.set_hatch(hatch)

    ax3.legend(bbox_to_anchor=(0.5, 1.25), ncol=4, loc='upper center', fontsize=18)
    plt.tight_layout()
    # 显示图形
    save_figure("huawei_dynamic_rl_throughput")
    # plt.show()

# 丢包率折线图
with plt.style.context(style):
    # 创建绘图
    fig3, ax3 = plt.subplots(figsize=figsize)
    ax3.grid(False)
    ax3.tick_params(axis='x', labelsize=tick_label_size)
    for tag in tags:
        group = rl_df[rl_df['tag'] == tag]
        sns.lineplot(x='step', y='timeout_rate', data=group, ax=ax3, zorder=2, marker=markers[tags.index(tag)], label=tag, color=custom_palette[tags.index(tag)])
    ax3.set_ylabel('Timeout Rate (%)')
    ax3.set_xlabel('Step')
    ax3.set_xticks(rl_df['step'].unique())

    ax3.tick_params(axis='y')
    # 调整Y轴范围
    # ax3.set_ylim(0, 1)
    for line in ax3.lines:
        line.set_linewidth(3)
        line.set_markersize(6)
    for marker in ax3.collections:
        marker.set_sizes([100])

    for hues, hatch in zip(ax3.containers, hatches):
        # set a different hatch for each time
        for hue in hues:
            hue.set_hatch(hatch)

    ax3.legend(bbox_to_anchor=(0.5, 1.25), ncol=4, loc='upper center', fontsize=18)
    plt.tight_layout()
    # 显示图形
    save_figure("huawei_dynamic_rl_timeout")
    # plt.show()

# 综合奖励折线图
with plt.style.context(style):
    # 创建绘图
    fig3, ax3 = plt.subplots(figsize=figsize)
    ax3.grid(False)
    ax3.tick_params(axis='x', labelsize=tick_label_size)
    for tag in tags:
        group = rl_df[rl_df['tag'] == tag]
        sns.lineplot(x='step', y='reward', data=group, ax=ax3, zorder=2, marker=markers[tags.index(tag)], label=tag, color=custom_palette[tags.index(tag)])
    ax3.set_ylabel('Reward')
    ax3.set_xlabel('Step')
    ax3.set_xticks(rl_df['step'].unique())

    ax3.tick_params(axis='y')
    # 调整Y轴范围
    # ax3.set_ylim(0.1, 0.7)
    for line in ax3.lines:
        line.set_linewidth(3)
        line.set_markersize(6)
    for marker in ax3.collections:
        marker.set_sizes([100])

    for hues, hatch in zip(ax3.containers, hatches):
        # set a different hatch for each time
        for hue in hues:
            hue.set_hatch(hatch)

    ax3.legend(bbox_to_anchor=(0.5, 1.25), ncol=4, loc='upper center', fontsize=18)
    plt.tight_layout()
    # 显示图形
    save_figure("huawei_dynamic_rl_reward")
    plt.show()