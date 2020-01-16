# -*- coding: UTF-8 -*- 
'''
@Author     :   Xu Junlin
@Software   :   PyCharm 2019.3 (Professional Edition)
'''
import matplotlib.pyplot as plt
import numpy as np
# Pollen data
all_data = np.array([[0.6204,0.7803,0.7583,0.7422,0.7752,0.5225,0.6684],
                    [0.7759,0.6994,0.7337,0.8203,0.6991,0.5031,0.7780],
                    [0.7211,0.6892,0.7122,0.6859,0.7091,0.4973,0.7032],
                    [0.6947,0.8452,0.7567,0.7778,0.8821,0.4763,0.8291],
                    [0.6909,0.8076,0.7738,0.6374,0.7604,0.4800,0.8843],
                    [0.7204,0.7244,0.8164,0.6878,0.6508,0.5461,0.8339],
                    [0.6344,0.6789,0.7002,0.7315,0.7483,0.5452,0.7534],
                    [0.6845,0.8134,0.7896,0.6414,0.7913,0.5028,0.6845],
                    [0.8050,0.8111,0.8512,0.8172,0.7501,0.4930,0.7059],
                    [0.6294,0.6306,0.7166,0.7350,0.8321,0.5176,0.7850]])

# Usoskin data
# all_data = np.array([[0.6097,0.6269,0.7305,0.3217,0.6484,0.4876,0.7715],
#                     [0.6746,0.7326,0.6834,0.4326,0.6515,0.3274,0.7167],
#                     [0.6733,0.6284,0.7081,0.4076,0.6492,0.4813,0.7433],
#                     [0.6012,0.6276,0.6069,0.5097,0.7115,0.3896,0.6805],
#                     [0.6687,0.7137,0.6876,0.4333,0.6506,0.3602,0.7099],
#                     [0.6302,0.6636,0.7026,0.5217,0.6412,0.4466,0.7694],
#                     [0.6565,0.6240,0.7001,0.4246,0.6479,0.3670,0.7704],
#                     [0.5722,0.6555,0.7016,0.4182,0.6620,0.4633,0.7258],
#                     [0.5987,0.6377,0.6059,0.3817,0.7612,0.3636,0.7570],
#                     [0.6279,0.7087,0.7318,0.4185,0.7315,0.4873,0.7616]])

labels = ["Raw", "DrImpute", "Saver", "scImpute","mcImpute","MAGIC","CMF-Impute"]
fig, axes = plt.subplots(figsize=(6, 3))

# box plot
bplot = axes.boxplot(all_data,
                         showmeans = False,
                         widths = 0.5,
                         notch= False,  # notch shape
                         vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         showfliers = False,
                         medianprops = {'linestyle':'-','color':'black'},
                         whiskerprops = {'linestyle':'--'},
                         labels=labels)

axes.set_title('(A) Pollen',loc = "left",fontsize = 12)
# axes.set_title('(B) Usoskin',loc = "left",fontsize = 12)
# fill with colors # lightblue
colors = ['pink', 'fuchsia', 'lime','salmon','mediumslateblue','gold','cyan']

for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

axes.set_xticklabels(labels,fontsize = 10)
axes.set_ylabel('ARI',fontsize = 10)
fig.tight_layout()
# sive .pdf
plt.savefig('/Users/xujunlin/Downloads/py_model/plot_xujunlin/Pollen_ARI_boxplot.pdf', dpi=600)
# plt.savefig('/Users/xujunlin/Downloads/py_model/plot_xujunlin/Usoskin_ARI_boxplot.pdf', dpi=600)
plt.show()