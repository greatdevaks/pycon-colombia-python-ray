import math, statistics, random, time, sys, locale
import ray
import numpy as np

def estimate_pi(num_samples):
    """
    Generate random samples for the x coordinate
    Generate random samples for the y coordinate
    Like Python's "zip(a,b)"; creates np.array([(x1,y1), (x2,y2), ...]).
    Create a predicate over all the array elements
    Selects only those "zipped" array elements inside the circle
    Return the number of elements inside the circle
    The Pi estimate
    """
    xs = np.random.uniform(low=-1.0, high=1.0, size=num_samples)
    ys = np.random.uniform(low=-1.0, high=1.0, size=num_samples)   
    xys = np.stack((xs, ys), axis=-1)                             
    inside = xs*xs + ys*ys <= 1.0                                  
    xys_inside = xys[inside]                                        
    in_circle = xys_inside.shape[0]                                 
    approx_pi = 4.0*in_circle/num_samples                           
    return approx_pi
  
@ray.remote
def ray_estimate_pi(num_samples):
    return estimate_pi(num_samples)

def main():
    # Estimate the value of PI with different sample points
    refs = [ray_estimate_pi.remote(n) for n in [100000, 10000000]]
    print(ray.get(refs))
    sys.stdout.flush()

if __name__ == "__main__":
    ray.init("ray://pycon-ray-cluster-00-ray-head:10001")
    main()
