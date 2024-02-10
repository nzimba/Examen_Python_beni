#!/usr/bin/env python
# coding: utf-8

# -----
# EXERCICE 1

# In[13]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)  # Crée une liste de 100 valeurs entre 0 et 1
y = x**5  # Calcul des valeurs y correspondantes à x⁵

plt.plot(x, y)  
plt.xlim(0, 1)  
plt.ylim(0, 1)  
plt.xlabel('x')  
plt.ylabel('y')  
plt.title('Courbe de l\'équation x⁵')  
plt.grid(True)  
plt.show() 

# Ajoute les droites délimitant le carré
plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], 'r-', label='Carré')
plt.title('La Figure d\'un carré')
plt.show()  # Affiche le graphique


# ----
# EXERCICE 2

# In[ ]:





# In[14]:


import matplotlib.pyplot as plt

class Curve:
     def __init__(self, start, stop, nbr_points=5432):
             self.start = start
             self.stop = stop
             self.nbr_points = nbr_points

     def _f(self, x):
             return x**5

     def _is_above_curve(self, x, y):
             return y > self._f(x)

     def plot_curve(self):
             x = []
             y = []
             for i in range(self.nbr_points):
                     x_val = self.start + (i / (self.nbr_points - 1)) * (self.stop - self.start)
                     y_val = self._f(x_val)
                     x.append(x_val)
                     y.append(y_val)
             plt.plot(x, y, color='black')

     def plot_points(self):
             for i in range(self.nbr_points):
                     x_val = self.start + (i / (self.nbr_points - 1)) * (self.stop - self.start)
                     y_val = self._f(x_val)
                     if self._is_above_curve(x_val, y_val):
                             plt.plot(x_val, y_val, 'bx')
                     else:
                             plt.plot(x_val, y_val, 'go')

     def calculate_surface_blue(self):
             blue_surface = 0
             for i in range(self.nbr_points - 1):
                     x_val1 = self.start + (i / (self.nbr_points - 1)) * (self.stop - self.start)
                     x_val2 = self.start + ((i + 1) / (self.nbr_points - 1)) * (self.stop - self.start)
                     y_val1 = self._f(x_val1)
                     y_val2 = self._f(x_val2)
                     if self._is_above_curve(x_val1, y_val1):
                             blue_surface += abs(x_val2 - x_val1) * (y_val2 - y_val1)
             return blue_surface

     def calculate_surface_vert(self):
             green_surface = 0
             for i in range(self.nbr_points - 1):
                     x_val1 = self.start + (i / (self.nbr_points - 1)) * (self.stop - self.start)
                     x_val2 = self.start + ((i + 1) / (self.nbr_points - 1)) * (self.stop - self.start)
                     y_val1 = self._f(x_val1)
                     y_val2 = self._f(x_val2)
                     if not self._is_above_curve(x_val1, y_val1):
                             green_surface += abs(x_val2 - x_val1) * (y_val2 - y_val1)
             return green_surface


# In[ ]:




