from PIL import Image
import scipy.cluster
import sklearn.cluster
import numpy

def dominant_colors(image):  # PIL image input

    image = image.resize((200, 200))      # optional, to reduce time
    ar = numpy.asarray(image)
    shape = ar.shape
    ar = ar.reshape(numpy.product(shape[:2]), shape[2]).astype(float)

    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_clusters=10,
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
working_image = Image.open("exampleImage1.jpg")

##Find the dominant RGB value
##Use k-means++ algorithm to cluster RGB Values

dominant_colors_ranked = dominant_colors(working_image)
##Find the top ranked color

most_dominant_color = dominant_colors_ranked[0]



