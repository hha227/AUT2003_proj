import matplotlib.pyplot as plt
import dataset4_noweight
import filter
# Make plot
num_bins=100

no_outliers = filter.removeOutliers(filter.removeFalseData(dataset4_noweight.data))

fig2, ax2 = plt.subplots()
ax2.hist(no_outliers, num_bins, density=1)
ax2.set_xlabel('Raw data')
ax2.set_ylabel('Probability density')
ax2.set_title('Histogram of raw data from HX711')
fig2.tight_layout()
fig2.show()
plt.savefig(r'no_outliers_data4_noweight.png', format='png')

# fig, ax = plt.subplots()
# ax.hist(data.data, num_bins, density=1)
# ax.set_xlabel('Raw data')
# ax.set_ylabel('Probability density')
# ax.set_title('Histogram of raw data from HX711')
# fig.tight_layout()
# fig.show()
# plt.savefig('histogram.png', format='png')
