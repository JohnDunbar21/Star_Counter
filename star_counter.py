from skimage import io
from skimage.feature import blob_log
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

"""
Reads the image from the root directory of the folder and creates a grayscale equivalent.
"""
image = io.imread("photo.jpg", plugin='matplotlib')
image_grayscale = rgb2gray(image)

"""
Generates a set of markers that establish a threshold for detection using the grayscale image.
"""
blobs_log = blob_log(image_grayscale, max_sigma=20, num_sigma=10, threshold=.02)

"""
Rest of code generates the figure and adds points over the plot as blue markers.
"""
fig = plt.figure("Approximate Number of Visible Stars")
ax = fig.add_subplot(1, 1, 1)

ax.imshow(image)
c_stars = 0
for blob in blobs_log:
    y, x, r = blob
    if r > 2:
        continue
    ax.add_patch(plt.Circle((x, y), 2*r, color="aqua", linewidth=2, fill=True))
    c_stars += 1
print("Number of stars: " + str(c_stars))
ax.set_axis_off()
ax.set_title(f"Approximate Number of Visible Stars: {c_stars}")
plt.savefig("approximate_visible_stars.png")
plt.tight_layout()
plt.show()