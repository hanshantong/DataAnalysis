# -*- coding: utf-8 -*-
import numpy as np
from patsy import dmatrices, dmatrix, demo_data
data = demo_data('a', 'b', 'x1', 'x2', 'y', 'z column')
print(f'data:\n{data}')
y, X = dmatrices("y ~ x1 + x2", data)
print(f'y={y}')
print(f"X={X}")

