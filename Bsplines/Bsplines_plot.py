import numpy as np
import matplotlib.pyplot as plt
from Bsplines_model import Bsplines_bases

class Bsplines_plots:
    """
    class for visualising the B-spline functions
    """
    
    def __init__(self, x_list, knot_points, spline_degree = 3):
        self.x_list = x_list
        self.knot_points = knot_points
        self.spline_degree = spline_degree
    
    def prepare_bases_for_plotting(self):
        """
        This function organises the output of the algorithm by basis function
        """
        
        basis_dict = {}
        # initialise basis_dict: There should be (no. of knot points - order of polynomial) bases
        no_of_bases = len(self.knot_points) + 2*(self.spline_degree) - (self.spline_degree + 1)
        for b in range(no_of_bases):
            basis_dict[b] = []
        
        for j in self.x_list:
            BS = Bsplines_bases(j, self.knot_points, self.spline_degree)
            BS_val = BS.collect_bases()
            for base in range(len(BS_val)):
                basis_dict[base].append(BS_val[base])
                
        return basis_dict 
    
    def plot_bases(self, image_plot_title):
        """
        This function plots the basis functions computed by the algorithm
        """
        basis_dict = self.prepare_bases_for_plotting()
        
        for key,base in basis_dict.items():
            plt.plot(self.x_list, basis_dict[key], label='$B_{%s,%s}(x)$'%(key,self.spline_degree))
            
        plt.legend(bbox_to_anchor=(1, 1.05))
        plt.title('Bspline Basis Functions, \n Polynomial degree = %s'%self.spline_degree)
#         plt.savefig('./plots/'+ image_plot_title + '-degree-'+str(self.spline_degree)+'.png', bbox_inches='tight')
        return


