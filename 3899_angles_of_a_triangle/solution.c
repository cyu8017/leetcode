// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

#include <stdlib.h>
#include <math.h>

static int cmpInt3899(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

double* internalAngles(int* sides, int sidesSize, int* returnSize) {
    (void)sidesSize;
    int s[3] = {sides[0], sides[1], sides[2]};
    qsort(s, 3, sizeof(int), cmpInt3899);
    int a = s[0], b = s[1], c = s[2];
    if (a + b <= c) { *returnSize = 0; return NULL; }
    double* out = malloc(3 * sizeof(double));
    double A = acos((double)(b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / M_PI;
    double B = acos((double)(a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / M_PI;
    double C = 180.0 - A - B;
    out[0] = A; out[1] = B; out[2] = C;
    *returnSize = 3;
    return out;
}
