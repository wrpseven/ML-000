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


int target_encoding_cpp(double* data, const long nrow, const long ncol, const long ypos, const long xpos, double* result) {

    printf("check01");
    int unique_cnt   = 11;
    long* count_list = new long[unique_cnt]();
    long* value_list = new long[unique_cnt]();


    printf("check02");
    for(long i=0;i<nrow;i++){
        long xvalue = (long)data[i*ncol+xpos];
        long yvalue = (long)data[i*ncol+ypos];
        count_list[xvalue] += 1;
        value_list[xvalue] += yvalue;    
    }

    printf("check03");
    for(long i=0;i<nrow;i++){
        long xvalue = (long)data[i*ncol+xpos];
        long yvalue = (long)data[i*ncol+ypos];
        result[i]  = (value_list[xvalue] - yvalue)/(count_list[xvalue] - 1);
    }

    printf("check04");
    if(count_list){
        delete []count_list;
    }
    if (value_list){
        delete []value_list;
    }

    return 0;
}
