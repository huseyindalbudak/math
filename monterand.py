# for minimum reqtangle integral any random points 

import numpy as np 

inside = 0
tot = 1000

for i in range(0, tot):
  # Generate random x, y in [0, 1].
  x = np.random.rand()
  y = np.random.rand()
    # Increment if inside unit circle.
  if (x*y) <0.9:     # 0.9 is area wanted
      inside += 1

square = float(inside) / total

# It works!
print(square)
