import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cv2
from tool.read_directory_files import get_basename


# ----- RGB -----

def showRGBspace(image_path, output_folder):
    img = cv2.imread(image_path)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    r, g, b = cv2.split(img_RGB)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    pixel_colors = img_RGB.reshape((np.shape(img_RGB)[0]*np.shape(img_RGB)[1], 3))
    norm = colors.Normalize(vmin=-1.0, vmax=1.0)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    plt.savefig(output_folder + "/" + "RGBspace_" + get_basename(image_path))
    # plt.show()

# ----- HSV -----


def showHSVspace(image_path, output_folder):
    img = cv2.imread(image_path)
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    h, s, v = cv2.split(img_HSV)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    pixel_colors = img_RGB.reshape((np.shape(img_RGB)[0]*np.shape(img_RGB)[1], 3))
    norm = colors.Normalize(vmin=-1.0, vmax=1.0)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")
    plt.savefig(output_folder + "HSVspace_" + get_basename(image_path))

