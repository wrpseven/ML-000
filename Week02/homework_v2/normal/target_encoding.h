#pragma once
#include <vector>
#include <cmath>
#include <iostream>
const double tres = 1e-5;


template<typename T, bool col_major=false>
class MatrixView{
public:
    T* data_pointer;
    const long nrow;
    const long ncol;

    MatrixView(T *data_pointer, const long nrow, const long ncol) : data_pointer(data_pointer), nrow(nrow),
                                                                    ncol(ncol) {}

    T &operator()(const int row, const int col) {
        if (col_major) {
            return data_pointer[row + col * nrow];
        } else {
            return data_pointer[col + row * ncol];
        }
    }

    T operator()(const int row, const int col) const {
        if (col_major) {
            return data_pointer[row + col * nrow];
        } else {
            return data_pointer[col + row * ncol];

        }
    }
};


std::vector<double> target_encoding_cpp(double* data, const long nrow, const long ncol, const long ypos, const long xpos, double* result) {
    
    int unique_cnt = 10;
    double* count_list = new double[unique_cnt]();
    double* value_list = new double[unique_cnt]();


    for(long i=0;i<nrow;i++){
        xvalue = data[i*ncol+xpos];
        yvalue = data[i*ncol+ypos];
        count_list[xvalue] += 1;
        value_list[xvalue] += yvalue;    
    }

    for(long i=0;i<nrow;i++){
        xvalue = data[i*ncol+xpos];
        yvalue = data[i*ncol+ypos];
        result[i]  = (value_list[xvalue] - yvalue)/(count_list[xvalue] - 1)
    }    

    if(count_list){
        delete []count_list;
    }
    if (value_list){
        delete []value_list;
    }

    return 0;
}
