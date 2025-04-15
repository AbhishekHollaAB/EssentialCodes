This repository contains codes that are useful to day to day Machine Learning/Deep Learning taks. Along with some other codes, that might end up helping you.

1. CompressWithResolution.py - This script helps reducing the file size of the image but without losing the dimensions. Quality of the image also reduces while compressing but that is adjustable.
2. CountContentInColumn.py - Read a CSV using Pandas and then get count of each unique element present in it.
3. ExtendCurvesAtEnds.py - If you have a thinned curve of 1px width and you want to add a certain number of pixel on either side to extend it, this is what you're looking for.
4. GenerateCubemapsFromPanorama.py - Convert a 360 equirectangular panoramic image into cubemaps.
5. GeneratePanoramaFromCubemaps.py - Convert a set of cubemaps into a 360 equirectangular panoramic image.
6. GetClassCountYOLO.py - Reads an annotation path and goes through each YOLO text file and then in the end returns the number of instances each class has.
7. LabelMe2YOLO.py - Converts a LabelMe JSON file into YOLO text file.
8. PDF2Image - Splits individual pages of a PDF into images.
9. RemoveAClassFromYOLOText.py - As the name indicates, in case you dont want a certain class to be trained, this will go through each text file and remove the said class.
10. SplitYOLOAnnotationVerticalHalves - While the use of this might be too specific, this divides an already annotated full image into two equal parts and re-writes the annotation file based on each half.
11. TrainTestSplit.py - Uses sklearn's train_test_split and made it more streamlined.
12. UniqueLabelsJSON.py - Gets the names of all classes present in each text file of a folder.
13. YOLO2LabelMe.py - Converts a YOLO text file into its JSON format thats readable in LabelMe.
14. YOLOPrediction.py - Basically YOLO's predict but customised.
15. YOLOTxt2ImageMask.py - Converts the YOLO text annotation into Mask Annotations that can be used to train for certain models.
