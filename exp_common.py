import numpy as np 
import copy
import pandas as pd 
import os 
from common import *
#distribution name 

hatch_style = ['x', '+', '//']
linestyle = ["dashed", "dotted", "dashdot", "dashed", "solid"]
# linemarker = ['o', '^', '*', 's', 'v']
linemarker = ["s", "D", "o", "^", "v", "X"]
#colors = ["#FBE5D6","#FFF2CC", "#A9D18E", "#7900CC", "#541E08", "#C82423", "#FF8884"]
#colors = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F", "#EDC948"]
colors = ["#006837", "#31A354", "#77C579",  "#77C579"]

plot_default_config = {
     "matplot_config" : {
        'linewidth' : 3,
        'markersize': 10,  
        'alpha' : 1,                    
        'zorder' : 10,
        'clip_on' : False,
    }
}

#configuration for workload num 
#workload_nums = np.array([8, 12, 16, 20, 24, 28, 32])

g_linewidth = 2.5
g_marker_size = 15

dist1 = 5
dist2 = 10 
dist3 = 15

dist1_label = "dist1"
dist2_label = "dist2"
dist3_label = "dist3"
baseline_label = "baseline"

ai_label = "AI"
ga_label = "GA"

dist1_color = colors[0]
dist2_color = colors[1]
dist3_color = colors[2]
baseline_color = colors[3]
ai_color = colors[0]
ga_color = colors[1]


dist1_maker = linemarker[0]
dist2_maker = linemarker[1]
dist3_maker = linemarker[2]
baseline_maker = None


dist1_style = linestyle[0]
dist2_style = linestyle[1]
dist3_style = linestyle[2]
baseline_style = linestyle[1]


plot_config_dist1 = copy.deepcopy(plot_default_config)
plot_config_dist2 = copy.deepcopy(plot_default_config)
plot_config_dist3 = copy.deepcopy(plot_default_config)
plot_config_baseline = copy.deepcopy(plot_default_config)

plot_config_dist1['matplot_config']['color'] = dist1_color
plot_config_dist1['matplot_config']['label'] = dist1_label
plot_config_dist1['matplot_config']['marker'] = dist1_maker
plot_config_dist1['matplot_config']['linestyle'] = dist1_style

plot_config_dist2['matplot_config']['color'] = dist2_color
plot_config_dist2['matplot_config']['label'] = dist2_label
plot_config_dist2['matplot_config']['marker'] = dist2_maker
plot_config_dist2['matplot_config']['linestyle'] = dist2_style

plot_config_dist3['matplot_config']['color'] = dist3_color
plot_config_dist3['matplot_config']['label'] = dist3_label
plot_config_dist3['matplot_config']['marker'] = dist3_maker
plot_config_dist3['matplot_config']['linestyle'] = dist3_style

plot_config_baseline['matplot_config']['color'] = baseline_color
#plot_config_baseline['matplot_config']['label'] = baseline_label
plot_config_baseline['matplot_config']['marker'] = baseline_maker
plot_config_baseline['matplot_config']['linestyle'] = baseline_style

#bar config
ai_hatch = hatch_style[0]
ga_hatch = hatch_style[1]

ai_bar_config = {
    "matplot_config" : {
        'color' : ai_color, 
        'edgecolor' : ai_color,  #edgecolor will override hatch color 
        'linewidth' : 1, 
        'label' : ai_label,   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '\\\\',
    },
    "hatch_config" : {
        'color' :  ai_color,
        'linewidth' : 0.8
    }
}

ga_bar_config = {
    "matplot_config" : {
        'color' : ga_color, 
        'edgecolor' : ga_color,  #edgecolor will override hatch color 
        'linewidth' : 1, 
        'label' : ga_label,   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '\\\\',
    },
    "hatch_config" : {
        'color' :  ai_color,
        'linewidth' : 0.8
    }
}


def add_suffix_all(value):
    return "%s-%s"%(value, "all")
def add_suffix_small(value):
    return "%s-%s"%(value, "small")

def read_dfs_node35():
    df_all = pd.read_csv(os.path.join(DATA_PATH, 'settings_all_node3.csv'))
    # df_small = pd.read_csv(os.path.join(DATA_PATH, 'settings_small_node3.csv'))
    # df_small['tag'] = df_small['tag'].apply(add_suffix_small)
    df_ga = pd.read_csv(os.path.join(DATA_PATH, 'GA_real_node35.csv'))
    df_rl = pd.read_csv(os.path.join(DATA_PATH, 'RL_node35.csv'))
    
    df = pd.concat([df_all, df_ga, df_rl], axis=0)
    df['throughput_mpps'] = df['avg_throughput_pkts'] / (1000 * 1000)
    df['timeout_rate_100'] =  df['timeout_rate'] * 100
    return df 

def read_dfs_node24():
    df_all = pd.read_csv(os.path.join(DATA_PATH, 'settings_all_node4.csv'))
    # df_small = pd.read_csv(os.path.join(DATA_PATH, 'settings_small_node4.csv'))
    # df_small['tag'] = df_small['tag'].apply(add_suffix_small)
    df_ga = pd.read_csv(os.path.join(DATA_PATH, 'GA_real_node24.csv'))
    
    df_rl = pd.read_csv(os.path.join(DATA_PATH, 'RL_node24.csv'))
    
    df = pd.concat([df_all, df_ga, df_rl], axis=0)
    df['throughput_mpps'] = df['avg_throughput_pkts'] / (1000 * 1000)
    df['timeout_rate_100'] =  df['timeout_rate'] * 100
    return df 