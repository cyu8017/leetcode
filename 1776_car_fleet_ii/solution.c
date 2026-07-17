// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* getCollisionTimes(int** cars, int carsSize, int* carsColSize, int* returnSize) {
    int n = carsSize;
    double* ans = (double*)malloc((size_t)n * sizeof(double));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = -1;
    for (int i = 0; i < n; i++) {
        ans[i] = -1.0;
    }
    for (int i = n - 1; i >= 0; i--) {
        int pos = cars[i][0];
        int speed = cars[i][1];
        while (top >= 0) {
            int j = stack[top];
            if (speed <= cars[j][1]) {
                top--;
                continue;
            }
            double t = (double)(cars[j][0] - pos) / (speed - cars[j][1]);
            if (ans[j] < 0 || t <= ans[j]) {
                ans[i] = t;
                break;
            }
            top--;
        }
        stack[++top] = i;
    }
    free(stack);
    *returnSize = n;
    return ans;
}
