from pdf2image import convert_from_path

i1 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/bc_validation.pdf'
i2 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/ml_validation.pdf'
# i3 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/neghmean_vs_poshmean.pdf'
# i4 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/normcdf_hmean.pdf'

images = convert_from_path(i1, 300)
for image in images:
    image.save('/Users/connormcdonald/Desktop/Masters/MIT807/Final/bc_validation.png')

images = convert_from_path(i2, 300)
for image in images:
    image.save('/Users/connormcdonald/Desktop/Masters/MIT807/Final/ml_validation.png')

# images = convert_from_path(i3, 300)
# for image in images:
#     image.save('neghmean_vs_poshmean.png')

# images = convert_from_path(i4, 300)
# for image in images:
#     image.save('normcdf_hmean.png')

print('done')