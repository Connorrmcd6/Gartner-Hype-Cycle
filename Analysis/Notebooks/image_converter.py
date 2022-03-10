from pdf2image import convert_from_path

i1 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/google_covid.pdf'
i2 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/3dprint.pdf'
i3 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/google_blockchain.pdf'
i4 = '/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Analysis/Figures/google_ml.pdf'

images = convert_from_path(i1, 300)
for image in images:
    image.save('covid.png')

# images = convert_from_path(i2, 300)
# for image in images:
#     image.save('3dprint.png')

# images = convert_from_path(i3, 300)
# for image in images:
#     image.save('google_blockchain.png')

# images = convert_from_path(i4, 300)
# for image in images:
#     image.save('google_ml.png')

print('done')