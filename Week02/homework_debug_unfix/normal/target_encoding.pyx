# distutils: language=c++
import numpy as np
cimport numpy as cnp
from libcpp.vector cimport vector
cdef extern from "target_encoding.h":
    int target_encoding_cpp(long*, const long, const long, const long, const long, double*);

def target_encoding(df, y_name, x_name):
    df_copy = df.copy(deep=True);
    ypos = df_copy.columns.get_loc(y_name);
    xpos = df_copy.columns.get_loc(x_name);

    result              = np.zeros((df_copy.shape[0]),dtype=np.float64);
    cdef cnp.ndarray[long, ndim=2, mode='fortran'] arg = np.asfortranarray(df_copy.values, dtype=np.int)
    cdef cnp.ndarray[double, ndim=1, mode='fortran'] dst = np.asfortranarray(result, dtype=np.float64)
    
    print("hello world");

    flag = target_encoding_cpp(&arg[0,0], df_copy.shape[0], df_copy.shape[1], ypos, xpos, &dst[0]);


    result = [1]*df.shape[0]
    return result

def target_encoding_new(df, y_name, x_name):
    df_copy = df.copy(deep=True);
    ypos = df_copy.columns.get_loc(y_name);
    xpos = df_copy.columns.get_loc(x_name);

    result              = np.zeros((df_copy.shape[0]),dtype=np.float64);
    #cdef cnp.ndarray[double, ndim=2, mode='fortran'] arg = np.asfortranarray(df_copy.values, dtype=np.float64)
    #cdef cnp.ndarray[double, ndim=1, mode='fortran'] dst = np.asfortranarray(result, dtype=np.float64)
   
    cdef long[:,:] arg_c    = df_copy.values
    cdef double[:] dst_c    = result
    print("hello world");

    flag = target_encoding_cpp(&arg_c[0,0], df_copy.shape[0], df_copy.shape[1], ypos, xpos, &dst_c[0]);


    result = [1]*df.shape[0]
    return result
