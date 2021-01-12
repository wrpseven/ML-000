#coding=utf-8
import numpy as np
import pandas as pd
import time
from line_profiler import LineProfiler
from fdmutils.common import debug_line
from fdmutils.common import get_tb_info
import pdb

from lib.target_encoding_cpp import target_encoding
from lib.target_encoding_cpp import target_encoding_new



def target_mean_v1(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result


def target_mean_v4(data, y_name, x_name):
    result = target_encoding(data, y_name, x_name)
    return result

def target_mean_v5(data, y_name, x_name):
    result = target_encoding_new(data, y_name, x_name)
    return result




def main():
    y = np.random.randint(2, size=(500, 1))
    x = np.random.randint(10, size=(500, 1))
    print("x.shape::",x.shape)
    print("y.shape::",y.shape)
    debug_line()

    
    data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
    print("data::",type(data),data.shape)
    print(data.head(3))
    debug_line()

    start = time.time() 
    result_1 = target_mean_v1(data, 'y', 'x')
    end   = time.time()
    print("target_mean_v1.cost %f" % (end-start))


    start = time.time()
    result_4 = target_mean_v4(data, 'y', 'x')
    end   = time.time()
    print("target_mean_v4.cost %f" % (end-start))
    debug_line()
    if True:
        print("result_4::",result_4[0:5])
        debug_line()


    start = time.time()
    result_5 = target_mean_v5(data, 'y', 'x')
    end   = time.time()
    print("target_mean_v5.cost %f" % (end-start))
    debug_line()
    if True:
        print("result_5::",result_5)
        debug_line()


    diff14 = np.linalg.norm(result_1 - result_4)
    print("diff14==",diff14)
    diff15 = np.linalg.norm(result_1 - result_5)
    print("diff15==",diff15)


if __name__ == '__main__':
    main()
