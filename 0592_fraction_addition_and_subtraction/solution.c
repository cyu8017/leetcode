// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static long long llabs64(long long x) {
    return x < 0 ? -x : x;
}

static long long gcd64(long long a, long long b) {
    a = llabs64(a);
    b = llabs64(b);
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

char* fractionAddition(char* expression) {
    long long numerator = 0;
    long long denominator = 1;
    int i = 0;
    int len = (int)strlen(expression);

    while (i < len) {
        int sign = 1;
        if (expression[i] == '+' || expression[i] == '-') {
            if (expression[i] == '-') {
                sign = -1;
            }
            i++;
        }
        long long a = 0;
        while (i < len && expression[i] >= '0' && expression[i] <= '9') {
            a = a * 10 + (expression[i] - '0');
            i++;
        }
        a *= sign;
        i++; // skip '/'
        long long b = 0;
        while (i < len && expression[i] >= '0' && expression[i] <= '9') {
            b = b * 10 + (expression[i] - '0');
            i++;
        }

        numerator = numerator * b + a * denominator;
        denominator *= b;
        long long g = gcd64(numerator, denominator);
        numerator /= g;
        denominator /= g;
    }

    char* result = (char*)malloc(64);
    sprintf(result, "%lld/%lld", numerator, denominator);
    return result;
}
