import numpy as np
import time

def simulateCircleTask(iterations):
    """
        Simulates the following:
        Sample three points uniformly on a circle. Connect all three points to a triangle.
        What is the likelihhod that the center of the circle is covered in the area of the triangle?
        
        Args:
        iterations: Number of experiements
        
        Returns:
        Prints the occupied time, as well as the approximated probability of above question.
        
    """
    start_time = time.time()
    start = 0
    ende = 2*np.pi
    inside = 0
    outside = 0
    for k in range(0, iterations):
        a = np.random.uniform(start, ende)
        b = np.random.uniform(start, ende)
        c = np.mod(np.random.uniform(start, ende) + np.pi, ende)
        if(np.abs(a - b) <= np.pi):
            q1 = np.minimum(a, b)
            q2 = np.maximum(a, b)
            q3 = 0
            q4 = 0
        else:
            q1 = np.maximum(a, b)
            q2 = ende
            q3 = start
            q4 = np.minimum(a, b)
        if((c >= q1 and c <= q2) or (c >= q3 and c <= q4)):
            inside += 1
        else:
            outside += 1
    end_time = time.time()
    print("Elapsed Time: " + str(end_time - start_time) + " seconds")
    print("Approximated Probability: " + str(float(inside) / float(iterations)))
    
simulateCircleTask(100000)
