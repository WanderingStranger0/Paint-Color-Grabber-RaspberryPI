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


working_image = Image.open("/home/ethan/Desktop/CompSci/370 Raspberry PI project/Paint-Color-Grabber-RaspberryPI/Picture to RGB Value/exampleImage3.jpeg")

##Find the dominant RGB value
##Use k-means++ algorithm to cluster RGB Values

dominant_colors_ranked = dominant_colors(working_image)
##Find the top ranked color

most_dominant_color = dominant_colors_ranked[0]
print(dominant_colors_ranked[0])
print(dominant_colors_ranked[1])
print(dominant_colors_ranked[2])

##Convert from dominant color to pantone, find whichever pantone value in MassiveColorsToRGBOrHex.csv is closest to our RGB, by using least squares regression



