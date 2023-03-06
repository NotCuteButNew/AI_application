import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
Point_A = np.array([0,0])
Point_B = np.array([1,9])
Line_AB = Point_B - Point_A
ax = plt.axes()
ax.arrow(Point_A[0],Point_A[1],Line_AB[0],Line_AB[1],head_width = 0.05,length_includes_head=True)                                                                                                                                                                     
R90= np.array([[0,-1],[1,0]])
LineAB = R90.dot(Line_AB)
print(Line_AB)
print(Line_AB.dot(LineAB))
ax.arrow(Point_A[0],Point_A[1],LineAB[0],LineAB[1],head_width = 0.05,length_includes_head=True)  
plt.axis('equal')
plt.show()