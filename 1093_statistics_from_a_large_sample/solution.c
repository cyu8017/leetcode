// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* sampleStats(int* count, int countSize, int* returnSize) {
    (void)countSize;
    long long total = 0;
    long long sum = 0;
    int minimum = -1, maximum = -1, mode = 0, modeCount = 0;
    for (int i = 0; i < 256; i++) {
        if (count[i]) {
            if (minimum < 0) {
                minimum = i;
            }
            maximum = i;
            total += count[i];
            sum += (long long)i * count[i];
            if (count[i] > modeCount) {
                modeCount = count[i];
                mode = i;
            }
        }
    }
    long long mid1 = (total + 1) / 2;
    long long mid2 = (total + 2) / 2;
    long long seen = 0;
    int first = -1, second = -1;
    for (int i = 0; i < 256; i++) {
        seen += count[i];
        if (first < 0 && seen >= mid1) {
            first = i;
        }
        if (second < 0 && seen >= mid2) {
            second = i;
            break;
        }
    }
    double* ans = (double*)malloc(5 * sizeof(double));
    ans[0] = (double)minimum;
    ans[1] = (double)maximum;
    ans[2] = (double)sum / (double)total;
    ans[3] = ((double)first + (double)second) / 2.0;
    ans[4] = (double)mode;
    *returnSize = 5;
    return ans;
}
