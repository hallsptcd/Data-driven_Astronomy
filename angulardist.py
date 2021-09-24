
# This angular_dist function calculates the angular distance between any two
# points on the celestial sphere given their right ascension and declination.

import numpy as np
def angular_dist(ra1, dec1, ra2, dec2):
  ra1_rad = np.radians(ra1)
  ra2_rad = np.radians(ra2)
  dec1_rad = np.radians(dec1)
  dec2_rad = np.radians(dec2)
  a = np.sin((np.abs(dec1_rad - dec2_rad))/2)**2
  b = np.cos(dec1_rad)*np.cos(dec2_rad)*np.sin(np.abs(ra1_rad - ra2_rad)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  d_deg = np.degrees(d)
  return d_deg

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))

