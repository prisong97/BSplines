import numpy as np
import matplotlib.pyplot as plt

class Bsplines_bases:
    """
    implemented based on De Boor's Algorithm outlined in 
    https://en.wikipedia.org/wiki/De_Boor%27s_algorithm
    """
    
    def __init__(self, x, knot_points, spline_degree = 3):
        self.x = x
        self.knot_points = knot_points
        self.spline_degree = spline_degree
        
    def add_knots(self):
        """
        prepend (and append) p=(spline_degree) knot points before (and after)
        """
        pre = [self.knot_points[0]] * self.spline_degree
        post = [self.knot_points[-1]] * self.spline_degree
        
        self.knot_points = pre + self.knot_points
        self.knot_points += post 
            
    
    def compute_bases(self, x, i, p):
        """
        compute the highest degree basis by control point indexed by i
        """
        #base case
        if p == 0:
            # check if x falls within the left-closed interval
            if (x >= self.knot_points[i]) and (x < self.knot_points[i+1]):
                return 1
            else:
                return 0
            
        #induction step
        if (self.knot_points[i+p+1] != self.knot_points[i+1]) and (self.knot_points[i+p] == self.knot_points[i]):
            
            # we are at the first B-spline
            alpha_2 = (self.knot_points[i+p+1]-x)/(self.knot_points[i+p+1] - self.knot_points[i+1])
            return alpha_2*self.compute_bases(x,i+1,p-1)
        
        if (self.knot_points[i+p] != self.knot_points[i]) and (self.knot_points[i+p+1] == self.knot_points[i+1]):
            
            # we are at the last B-spline
            alpha_1 = (x-self.knot_points[i])/(self.knot_points[i+p] - self.knot_points[i])
            return alpha_1*self.compute_bases(x,i,p-1)
            
        if (self.knot_points[i+p] == self.knot_points[i]) and (self.knot_points[i+p+1] == self.knot_points[i+1]):
            return 0
        alpha_1 = (x-self.knot_points[i])/(self.knot_points[i+p] - self.knot_points[i])
        alpha_2 = (self.knot_points[i+p+1]-x)/(self.knot_points[i+p+1] - self.knot_points[i+1])
               
        return alpha_1*self.compute_bases(x,i,p-1) + alpha_2*self.compute_bases(x,i+1,p-1)
    
    def collect_bases(self):
        """
        main function to run
        """
        self.add_knots()
        basis_functions_list = []
        
        for i in range(len(self.knot_points)-(self.spline_degree+1)):
            basis_function = self.compute_bases(self.x, i, self.spline_degree)
            basis_functions_list.append(basis_function)
            
        return basis_functions_list
    
    
