from pdf2image import convert_from_path

i1 = '/Users/connormcdonald/Downloads/80-20.pdf'
i2 = '/Users/connormcdonald/Downloads/zipf_sample.pdf'
# i3 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/neghmean_vs_poshmean.pdf'
# i4 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/normcdf_hmean.pdf'

images = convert_from_path(i1, 300)
for image in images:
    image.save('/Users/connormcdonald/Downloads/80-20.png')

images = convert_from_path(i2, 300)
for image in images:
    image.save('/Users/connormcdonald/Downloads/zipf_sample.png')

# images = convert_from_path(i3, 300)
# for image in images:
#     image.save('neghmean_vs_poshmean.png')

# images = convert_from_path(i4, 300)
# for image in images:
#     image.save('normcdf_hmean.png')

print('done')