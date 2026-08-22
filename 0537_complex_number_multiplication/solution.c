// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void parse_number(const char* num, int* real, int* imag) {
    const char* plus = strchr(num, '+');
    *real = atoi(num);
    *imag = atoi(plus + 1);
}

char* complexNumberMultiply(char* num1, char* num2) {
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    parse_number(num1, &a, &b);
    parse_number(num2, &c, &d);

    const int real = a * c - b * d;
    const int imag = a * d + b * c;

    char* result = (char*)malloc(64);
    if (!result) {
        return NULL;
    }
    snprintf(result, 64, "%d+%di", real, imag);
    return result;
}
