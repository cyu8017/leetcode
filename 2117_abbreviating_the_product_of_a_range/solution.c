// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

char* abbreviateProduct(int left, int right) {
    int twos = 0, fives = 0;
    for (int i = left; i <= right; i++) {
        int x = i;
        while (x % 2 == 0) { twos++; x /= 2; }
        while (x % 5 == 0) { fives++; x /= 5; }
    }
    int zeros = twos < fives ? twos : fives;
    const long long MOD = 100000000000LL;
    long long prod = 1;
    int extra2 = twos - zeros, extra5 = fives - zeros;
    double logSum = 0.0;
    for (int i = left; i <= right; i++) {
        int x = i;
        while (x % 2 == 0) x /= 2;
        while (x % 5 == 0) x /= 5;
        prod = (prod * x) % MOD;
        logSum += log10((double)x);
    }
    for (int i = 0; i < extra2; i++) { prod = (prod * 2) % MOD; logSum += log10(2.0); }
    for (int i = 0; i < extra5; i++) { prod = (prod * 5) % MOD; logSum += log10(5.0); }
    double fullLog = 0.0;
    for (int i = left; i <= right; i++) fullLog += log10((double)i);
    int digits = (int)fullLog + 1;
    char* out = (char*)malloc(64);
    if (digits <= 10) {
        long long p = 1;
        for (int i = left; i <= right; i++) p *= i;
        sprintf(out, "%lld", p);
        return out;
    }
    double frac = logSum - floor(logSum);
    long long prefix = (long long)pow(10.0, frac + 4.0);
    long long suffix = prod % 100000;
    sprintf(out, "%llde%d%05lld", prefix, zeros, suffix);
    return out;
}
