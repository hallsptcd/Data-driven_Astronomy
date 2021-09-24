
# This load_fits function loads a FITS file, and plots a 2D image.

def load_fits(file):
  import numpy as np
  import matplotlib.pyplot as plt
  from astropy.io import fits
  hdulist = fits.open(file)
  data = hdulist[0].data
  n = len(data)
  m = np.unravel_index(np.argmax(data), data.shape)
  return m


if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

