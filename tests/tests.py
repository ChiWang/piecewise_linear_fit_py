import numpy as np
import unittest
import pwlf

class test_everything(unittest.TestCase):
    # let's just test all of my use cases...
    # def __init__(self):
    x_small = np.array((0.0,1.0,1.5,2.0))
    y_small = np.array((0.0,1.0,1.1,1.5))

    # def test_is_five_prime(self):
    #     """Is five successfully determined to be prime?"""
    #     self.assertTrue(is_prime(5))
    
    def test_break_point_spot_on(self):
        # check that I can fit when break poitns spot on a
        my_fit1 = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        x0 = self.x_small.copy()
        ssr = my_fit1.fitWithBreaks(x0)
        self.assertTrue(np.isclose(ssr,0.0))
    
    def test_break_point_diff_x0_0(self):
        # check diff loc
        my_fit2 = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        x0 = self.x_small.copy()        
        x0[1] = 1.00001
        x0[2] = 1.50001
        ssr2 = my_fit2.fitWithBreaks(x0)
        self.assertTrue(np.isclose(ssr2,0.0))
    
    def test_break_point_diff_x0_1(self):
        # check if my duplicate is in a different location
        x0 = self.x_small.copy()
        my_fit3 = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        x0[1] = 0.9
        ssr3 = my_fit3.fitWithBreaks(x0)
        self.assertTrue(np.isclose(ssr3,0.0))
        
    def test_break_point_diff_x0_2(self):
        # check if my duplicate is in a different location
        x0 = self.x_small.copy()
        my_fit4 = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        x0[1] = 1.1
        ssr4 = my_fit4.fitWithBreaks(x0)
        self.assertTrue(np.isclose(ssr4,0.0))
        
    def test_break_point_diff_x0_3(self):
        # check if my duplicate is in a different location
        x0 = self.x_small.copy()
        my_fit5 = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        x0[2] = 1.6
        ssr5 = my_fit5.fitWithBreaks(x0)
        self.assertTrue(np.isclose(ssr5,0.0))
        
    def test_break_point_diff_x0_4(self):   
        # check if my duplicate is in a different location
        x0 = self.x_small.copy()
        my_fit6 = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        x0[2] = 1.4
        ssr6 = my_fit6.fitWithBreaks(x0)
        self.assertTrue(np.isclose(ssr6,0.0))
    
    def test_diff_evo(self):
        myPWLF = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        res = myPWLF.fit(4, disp=False)
        self.assertTrue(np.isclose(res[0],0.0))
    
    def test_custom_opt(self):
        myPWLF = pwlf.piecewise_lin_fit(self.x_small,self.y_small)
        xGuess = np.array((0.9, 1.1))
        from scipy.optimize import minimize
        res = minimize(myPWLF.fitWithBreaksOpt, xGuess)
        print(res)
        self.assertTrue(np.isclose(res['fun'],0.0))

        

if __name__ == '__main__':
    unittest.main()