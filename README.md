# passportPhoto
Passport Photo generation related

# prerequisites
Just run `python3 -m pip install -r requirements.txt`

# passportPhotoGen.py 
Scales input image to Australian Passport dimensions (37mm by 47mm) & outputs it for 4x6 printing format. It will make multiple copies to use up all the 4x6 space, but allow margins for cutting.

- usage: `passportPhotoGen.py <input_filename>` -  Output filename: <input_filname>[_f].jpg

iPhone OS and Windows Paint both have 'remove background'/'select foreground' features that make it easier to make the background white. 
