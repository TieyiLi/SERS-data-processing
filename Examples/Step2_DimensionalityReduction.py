import numpy as np
import matplotlib.pyplot as plt
from Tools.Utils import Utils, Visualization
from Tools.AdditionalProcessing import AdditionalProcessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

uti = Utils()
addprep = AdditionalProcessing()

##===================================================Start Running===========================================================##
##------------------------------------------------input data dictionary------------------------------------------------------##

data_dict_path = r'/Users/tieyili/Desktop/data11_10_21_SpikedSalivaBlindTest_2ndRoundTest_Sub.npy'
data_matrix, label, group, sample_name, raman_shift, map_index = addprep.input_data(data_dict_path)

##------------------------------------------------input data dictionary------------------------------------------------------##

X = uti.smoothing(data_matrix)

##------------------------------------------------dimensionality reduction---------------------------------------------------##

##......................................................TSNE or PCA..........................................................##
# reduce = TSNE(n_components=2, perplexity=10, learning_rate=50, n_iter=1500, metric='euclidean')
reduce = PCA(n_components=2)
X_reduced = reduce.fit_transform(X)

##..........................................................LDA..............................................................##
# reduce = LDA(n_components=2) # Only applicable to multi-classes !!!
# reduce.fit(X, label) # you can switch between 'label' or 'group' depending on your distinguishing target
# X_reduced = reduce.transform(X)

##.......................................................Plotting............................................................##
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
viz = Visualization()
viz.scatter_plot(ax=ax, x=X_reduced[:, 0], y=X_reduced[:, 1], label=label, marker='o') # 'label' parameter muct be the same as the one in line#31
ax.legend(labels=['B.1.1.7', 'Delta', 'WA']) # provide detailed legend for each sample
ax.set_xlabel('LD1', fontsize=13, fontstyle='italic')
ax.set_ylabel('LD2', fontsize=13, fontstyle='italic')
ax.set_title('Linear Discriminant Analysis', fontsize=16)
plt.show()
