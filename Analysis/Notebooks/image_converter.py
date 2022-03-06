from pdf2image import convert_from_path
images = convert_from_path('/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/zipf_plot.pdf', 300)
for image in images:
    image.save('zipfs_plot.png')

print('done')