# distutils: language=c++
import numpy as np
cimport numpy as cnp
from libcpp.vector cimport vector
cdef extern from "target_encoding.h":
    int target_encoding_cpp(double*, const long, const long, const long, const long, double*);

def target_encoding(df, y_name, x_name, result):
    df_copy = df.copy(deep=True);
    ypos = df_copy.columns.get_loc(y_name);
    xpos = df_copy.columns.get_loc(x_name);

    cdef double arg     = df_copy.values[0,0];
    result              = np.zeros((df_copy.shape[0],1),dtype=np.float64);
    cdef double dst     = result[0]
    target_encoding_cpp(&arg, df_copy.shape[0], df_copy.shape[1], ypos, xpos, &dst);
   
    return result
