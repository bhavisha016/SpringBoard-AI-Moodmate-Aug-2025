import numpy as np 

a = np.array([10, 20, 30, 40]) 
b = np.array([1, 2, 3, 4]) 

# Element-wise addition 
print("Addition:", a + b)  
# 👉 [11 22 33 44]

# Element-wise subtraction 
print("Subtraction:", a - b)  
# 👉 [ 9 18 27 36]

# Element-wise multiplication 
print("Multiplication:", a * b)  
# 👉 [10 40 90 160]

# Element-wise division 
print("Division:", a / b)  
# 👉 [10. 10. 10. 10.]

# Square root 
print("Square root of a:", np.sqrt(a))  
# 👉 [3.16227766 4.47213595 5.47722558 6.32455532]

# Exponentiation 
print("a squared:", np.power(a, 2))  
# 👉 [ 100  400  900 1600]
