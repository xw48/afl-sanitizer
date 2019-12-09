
#include<stdlib.h>
#include<stdbool.h>
#include<stdio.h>
#include<string.h>
#include<math.h>

#include"pearsoncorrelation.h"

//--------------------------------------------------------
// FUNCTION PROTOTYPES
//--------------------------------------------------------
static double arithmetic_mean(double* data, int size);
static double mean_of_products(double* data1, double* data2, int size);
static double standard_deviation(double* data, int size);

//--------------------------------------------------------
// FUNCTION pearson_correlation
//--------------------------------------------------------
double pearson_correlation(double* independent, double* dependent, int size)
{
    double rho;

    // covariance
    double independent_mean = arithmetic_mean(independent, size);
    double dependent_mean = arithmetic_mean(dependent, size);
    double products_mean = mean_of_products(independent, dependent, size);
    double covariance = products_mean - (independent_mean * dependent_mean);

    // standard deviations of independent values
    double independent_standard_deviation = standard_deviation(independent, size);

    // standard deviations of dependent values
    double dependent_standard_deviation = standard_deviation(dependent, size);

    // Pearson Correlation Coefficient
    rho = covariance / (independent_standard_deviation * dependent_standard_deviation);

    return rho;
}

//--------------------------------------------------------
// FUNCTION arithmetic_mean
//--------------------------------------------------------
static double arithmetic_mean(double* data, int size)
{
    double total = 0;

    // note that incrementing total is done within the for loop
    int i;
    for(i = 0; i < size; total += data[i], i++);

    return total / size;
}

//--------------------------------------------------------
// FUNCTION mean_of_products
//--------------------------------------------------------
static double mean_of_products(double* data1, double* data2, int size)
{
    double total = 0;

    // note that incrementing total is done within the for loop
    int i;
    for(i = 0; i < size; total += (data1[i] * data2[i]), i++);

    return total / size;
}

//--------------------------------------------------------
// FUNCTION standard_deviation
//--------------------------------------------------------
static double standard_deviation(double* data, int size)
{
    double squares[size];

    int i;
    for(i = 0; i < size; i++)
    {
        squares[i] = pow(data[i], 2);
    }

    double mean_of_squares = arithmetic_mean(squares, size);
    double mean = arithmetic_mean(data, size);
    double square_of_mean = pow(mean, 2);
    double variance = mean_of_squares - square_of_mean;
    double std_dev = sqrt(variance);

    return std_dev;
}
