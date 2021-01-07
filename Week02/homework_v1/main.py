#coding=utf-8
import numpy as np
import pandas as pd
import time
from line_profiler import LineProfiler
from fdmutils.common import debug_line
from fdmutils.common import get_tb_info


def target_mean_v1(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result


def target_mean_v2(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    value_dict = dict()
    count_dict = dict()
    for i in range(data.shape[0]):
        if data.loc[i, x_name] not in value_dict.keys():
            value_dict[data.loc[i, x_name]] = data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] = 1
        else:
            value_dict[data.loc[i, x_name]] += data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] += 1
    if True:
        print("value_dict::",value_dict)
        print("count_dict::",count_dict)
    
    for i in range(data.shape[0]):
        result[i] = (value_dict[data.loc[i, x_name]] - data.loc[i, y_name]) / (count_dict[data.loc[i, x_name]] - 1)
    return result



@profile
def target_mean_v3(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    
    fieldkey_dict = dict()
    for i,element in enumerate(data.columns):
        fieldkey_dict[element] = i

    value_dict = dict()
    count_dict = dict()
    for i in range(data.shape[0]):
       x_namevalue = data.values[i,fieldkey_dict[x_name]]
       value_dict[x_namevalue] = 0
       count_dict[x_namevalue] = 0

    for i in range(data.shape[0]):
        x_namevalue = data.values[i,fieldkey_dict[x_name]]      ##data.loc[i,x_name]
        y_namevalue = data.values[i,fieldkey_dict[y_name]]      ##data.loc[i,y_name]
        value_dict[x_namevalue] += y_namevalue
        count_dict[x_namevalue] += 1
    if True:
        print("value_dict::",value_dict)
        print("count_dict::",count_dict)

    for i in range(data.shape[0]):
        x_namevalue = data.values[i,fieldkey_dict[x_name]]      ##data.loc[i,x_name]
        y_namevalue = data.values[i,fieldkey_dict[y_name]]      ##data.loc[i,y_name]
        result[i] = (value_dict[x_namevalue] - y_namevalue) / (count_dict[x_namevalue] - 1)
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
    result_2 = target_mean_v2(data, 'y', 'x')
    end   = time.time()
    print("target_mean_v2.cost %f" % (end-start))
    debug_line()

    start = time.time()
    result_3 = target_mean_v3(data, 'y', 'x')
    end   = time.time()
    print("target_mean_v3.cost %f" % (end-start))
    debug_line()



    diff12 = np.linalg.norm(result_1 - result_2)
    print("diff12==",diff12)
    diff13 = np.linalg.norm(result_1 - result_3)
    print("diff13==",diff13)


if __name__ == '__main__':
    main()
