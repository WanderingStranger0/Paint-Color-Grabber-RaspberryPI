from PIL import Image
import scipy.cluster
import sklearn.cluster
import numpy

def dominant_colors(image):  # PIL image input

    image = image.resize((200, 200))
    ar = numpy.asarray(image)
    shape = ar.shape
    ar = ar.reshape(numpy.prod(shape[:2]), shape[2]).astype(float)

    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_init = 3,
        n_clusters=3,
        init="k-means++",
        max_iter=20,
        random_state=1000
    ).fit(ar)
    codes = kmeans.cluster_centers_

    vecs, _dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, _bins = numpy.histogram(vecs, len(codes))    # count occurrences

    colors = []
    for index in numpy.argsort(counts)[::-1]:
        colors.append(tuple([int(code) for code in codes[index]]))
    return colors                    # returns colors in order of dominance

def run():
    working_image = Image.open("/home/derrick/cs370/rawimage.jpg")

##Find the dominant RGB value
##Use k-means++ algorithm to cluster RGB Values

    dominant_colors_ranked = dominant_colors(working_image)
##Find the top ranked color

    most_dominant_color = dominant_colors_ranked[0]
    #print(dominant_colors_ranked[0])
    #print(dominant_colors_ranked[1])
    #print(dominant_colors_ranked[2])
    return most_dominant_color

##Convert from dominant color to pantone, find whichever pantone value in MassiveColorsToRGBOrHex.csv is closest to our RGB, by using least squares regression


