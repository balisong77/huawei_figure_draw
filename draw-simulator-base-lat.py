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

x_tick_labels = ["ip6","ip4_nat","ip4_wo_nat","igmp","arp","tap","icmp"]
targets =  ["%s_avg_lat_ns"%x for x in x_tick_labels]
target_row = 128
## data 
# 读取 CSV 文件

df_base = pd.read_csv(os.path.join(DATA_PATH, 'settings_all_detail_node3.csv'))
real_latencies = df_base[df_base["tag"]==target_row].loc[:, targets].to_numpy()[0] / 1000

df_simulator = pd.read_csv(os.path.join(DATA_PATH, 'simulator_base.csv'))
sim_latencies = df_simulator[df_simulator["tag"]==target_row].loc[:, targets].to_numpy()[0] / 1000

fig_config = {
    'xlabel' : 'Workload',   #x轴标签名
    'ylabel_0' : 'Latency (us)' , #y轴标签名
    'bar_width' : 0.020, #每一根柱子的宽度
    'text_size' : 19,
    'bar_line_width' : 1,
    'gridspec_kw' : {
        "wspace" : 0.145,
        "hspace" : 1,
    },
    "xtick_label_conf": {
         "rotation" : 30,
         "ha" : "center",
    },
    "bar_interval" : 0.06,
    "bar_edge": 0.038,
    "legned_conf" : {
        "loc" : "upper left",
        "bbox_to_anchor" : (0.35, 1.1),
        "ncols" : 3,
    },
    "hatch_line_width" : 1
}

real_bar_config = {
    "matplot_config" : {
        'color' : "white", 
        'edgecolor' : colors[0],  #edgecolor will override hatch color 
        'linewidth' : 1, 
        'label' : "Real",   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : hatch_style[0],
    },
    "hatch_config" : {
        'color' :  colors[0],
        'linewidth' : 3
    }
}

sim_bar_config = {
    "matplot_config" : {
        'color' : "white", 
        'edgecolor' : colors[1],  #edgecolor will override hatch color 
        'linewidth' : 1, 
        'label' : "Simulator",   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : hatch_style[1],
    },
    "hatch_config" : {
        'color' :  colors[1],
        'linewidth' : 3
    }
}

# 绘图
with plt.style.context(styles):   
    sns.set_context("paper", font_scale=2.5)
    fig, ax1 = plt.subplots(figsize=(12, 8))
    sns.set_context("paper", font_scale=3.2)
    width = fig_config['bar_width']
    x_tick, _, right_edge = cal_bar_xticks(fig_config["bar_edge"] + width/2, 
       len(x_tick_labels), width , interval=fig_config["bar_interval"])
    x = np.array(x_tick)
    
    set_hatch(**real_bar_config["hatch_config"])
    __barcontainer = ax1.bar(x - width/2, np.array(real_latencies), width, **real_bar_config["matplot_config"])
    set_bar_edgecolor_to_black(__barcontainer)
    set_hatch(**ga_bar_config["hatch_config"])
    __barcontainer = ax1.bar(x + width/2, np.array(sim_latencies), width, **sim_bar_config["matplot_config"])
    set_bar_edgecolor_to_black(__barcontainer)
    
    
    for p in ax1.patches:
        ax1.text(
            p.get_x() + p.get_width() / 2,  # x 坐标：柱子中心
            p.get_height() + 0.04,           # y 坐标：柱子高度 + 偏移量
            f'{p.get_height():.2f}',        # 显示的文本（数值）
            ha='center',                    # 水平对齐方式
            va='bottom',                    # 垂直对齐方式
            fontsize=8                     # 字体大小
        )
    
    # sns.barplot(ax = ax1, x = x, y = throughput_mvpp, color=colors[1], width=width)
    # sns.barplot(ax = ax1, x = x + width, y = throughput_mvpp_edf, color=colors[2], width=width)
    
    ax1.set_xlabel(fig_config["xlabel"])
    ax1.set_ylabel(fig_config["ylabel_0"])
    ax1.set_xticks(x_tick, x_tick_labels, rotation=30)
    ax1.set_ylim(0, 1500)
    
    ax1.legend(loc="upper center", ncol=2)
    
     
   
    plt.subplots_adjust(hspace=0.3)
    fig.tight_layout()
    save_figure('simulator-base-lat')
    # plt.show()