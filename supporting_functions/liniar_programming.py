# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:36:52 2020

@author: jacob
"""
import pandas as pd
import numpy as np
from pulp import LpProblem, LpStatus, lpSum, LpVariable




def liniary_optimization(max_or_min: int = 1):
    
    model = LpProblem(name="current_task", sense=max_or_min2)
    x = {i: LpVariable(name="x{}".format(i), lowBound=0) for i in range(1, 5)}
    
    model += (1*x[1] + 1*x[2] + 1*x[3] + 1*x[4] <= 50, "manpower")
    model += (3*x[1] + 2*x[2] + 1*x[3] + 0*x[4] <= 100, "material_A")
    model += (0*x[1] + 1*x[2] + 2*x[3] + 3*x[4] <= 90,  "material_B")
    
    objective_function =  20*x[1] + 12*x[2] + 40*x[3] +  25*x[4]
    model += objective_function
    print(model)
    
    model.solve()
    
    print("status: {}, {}".format(model.status, LpStatus[model.status]))
    
    print("objective: {}".format(model.objective.value()))

    for var in model.variables():
        print("{}: {}".format(var.name, var.value()))

    for name, constraint in model.constraints.items():
        print("{}: {}".format(name, constraint.value()))







if __name__ == '__main__':
    
