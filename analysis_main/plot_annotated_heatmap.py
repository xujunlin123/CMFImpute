'''
@Author     :   Xu Junlin
@Software   :   PyCharm 2019.3 (Professional Edition)
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 12}
    font2 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 14}
    ax.set_xticklabels(col_labels,font1)
    ax.set_yticklabels(row_labels,font2)

    # modify this part and change the label direction
    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=False, bottom=True,
                   labeltop=False, labelbottom=True)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar

def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

# input data ARI
datasets = ["Usoskin", "Pollen", "Loh", "IPSC", "Zeisel"]
methods = ["Raw", "DrImpute", "Saver", "scImpute","mcImpute","MAGIC","CMF-Impute"]
results = np.array([[0.916,0.812,0.835,0.444,0.800,0.351,0.932],
                    [0.863,0.934,0.956,0.854,0.933,0.598,0.960],
                    [0.913,0.894,0.971,0.982,0.976,0.753,0.976],
                    [0.791,0.779,0.803,0.577,0.836,0.484,0.845],
                    [0.775,0.712,0.648,0.715,0.842,0.166,0.845]])

# # # input data NMI
# datasets = ["Usoskin", "Pollen", "Loh", "IPSC", "Zeisel"]
# methods = ["Raw", "DrImpute", "Saver", "scImpute","mcImpute","MAGIC","CMF-Impute"]
# results = np.array([[0.887,0.793,0.829,0.510,0.814,0.447,0.915],
#                     [0.925,0.952,0.952,0.929,0.945,0.755,0.957],
#                     [0.929,0.918,0.959,0.973,0.965,0.788,0.965],
#                     [0.789,0.772,0.811,0.699,0.863,0.519,0.874],
#                     [0.730,0.699,0.679,0.741,0.811,0.287,0.795]])

fig, ax = plt.subplots(figsize=(9.2,5))
im, cbar = heatmap(results, datasets, methods, ax=ax,
                   cmap=plt.get_cmap("GnBu"))

texts = annotate_heatmap(im, valfmt="{x:.3f}",size = 16)
fig.tight_layout()
# sive ARI.pdf or NMI.pdf
plt.savefig('/Users/xujunlin/Downloads/py_model/plot_xujunlin/ARI.pdf', dpi=600)
plt.show()