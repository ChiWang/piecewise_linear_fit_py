import numpy as np
import pwlf

x = np.array((0.0,1.0,1.5,2.0))
y = np.array((0.0,1.0,1.1,1.5))

my_fit1 = pwlf.piecewise_lin_fit(x,y)
x0 = x.copy()
# check that I can fit when break poitns spot on a
ssr = my_fit1.fitWithBreaks(x0)

# check that i can fit when I slightly modify x0
my_fit2 = pwlf.piecewise_lin_fit(x,y)
x0[1] = 1.00001
x0[2] = 1.50001
ssr2 = my_fit2.fitWithBreaks(x0)

# check if my duplicate is in a different location
x0 = x.copy()
my_fit3 = pwlf.piecewise_lin_fit(x,y)
x0[1] = 0.9
ssr3 = my_fit3.fitWithBreaks(x0)

# check if my duplicate is in a different location
x0 = x.copy()
my_fit4 = pwlf.piecewise_lin_fit(x,y)
x0[1] = 1.1
ssr4 = my_fit4.fitWithBreaks(x0)

# check if my duplicate is in a different location
x0 = x.copy()
my_fit5 = pwlf.piecewise_lin_fit(x,y)
x0[2] = 1.6
ssr5 = my_fit5.fitWithBreaks(x0)

# check if my duplicate is in a different location
x0 = x.copy()
my_fit6 = pwlf.piecewise_lin_fit(x,y)
x0[2] = 1.4
ssr6 = my_fit6.fitWithBreaks(x0)
