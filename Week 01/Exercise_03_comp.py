# -*- coding: utf-8 -*-
"""
Exercise 03: Chapter 03, Kinder & Nelson

A common way to determine the value of a function is to sum over a series. 
For example, the Maclaurin series for sin(x) is

    sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...

Perform a series expansion to derive the equation above. Next, write down 
a general expression for the sum of the series that is valid between n = 0 
and n = N, where N ≥ 0. This will serve as your algorithm for summing 
the series.

One problem with the algorithm is that we do not know which value 
of N is suitable when calcualting the series. Instead of guessing, have 
your code proceed with the summation until the Nth term contributes a 
negligible amount to the final summation, say 1 part in 10**8.

Before writing any lines of code, discuss an approach with your neighbor 
and write out on paper how your code should proceed. Code up your approach 
in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(x) to 
      derive the equation in the README. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of x, the series converges.
   6. Which value for N was required to reach the desired precision and
      obtain convergence?
   7. Compare your results to the value determined using NumPy's sine 
      function.
   8. Steadily increase x and write down the relative error between your
      calculated value for sin(x) and the NumPy function's value. 
   9. What do you notice about the relative error?
  10. Will there be a time when the series does not converge? Make a plot
      of the relative error vs x to support your answer.

Created on Tue Aug 20 11:02:00 2019

@author: gafeiden
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#in a for loop:

x_val = np.arange(0,50,0.1)
#x_val = [0.01,0.5,5,50,500]
summation = 0
relative_errors = []

approx_y = []
actual_y = []

for x in x_val:
    print('x = ',x)
    print("sin(x) = ", np.sin(x))
    actual_y.append(np.sin(x))
    for n in range(100):
    
        denomenator = math.factorial((2*n)+1)
    
        iteration = (((-1)**(n))*(x**((2*n)+1)))/denomenator
    
        summation = summation + iteration
        
    
        if np.abs(iteration) <= (1/(10**8)):
            print('sin(x) approx ', summation)
            print('sin(x) approximation complete ', n)
            break
    
    abs_err = np.sin(x) - summation
    rel_err = abs_err/x
    relative_errors.append(rel_err)
    approx_y.append(summation)

plt.plot(x_val, relative_errors,  '.', lw=1)
plt.xlabel('x')
plt.ylabel('relative error')
plt.show()

#plt.plot(x_val, actual_y, '.', lw = 1, label = 'f(x) = sin(x)')
plt.plot(x_val, approx_y, '.', lw = 1, label = 'sin(x) approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
        

    #print("sin(x) approx ", summation)





