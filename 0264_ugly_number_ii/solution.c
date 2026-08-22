// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

#include <stdlib.h>

static int min_int(int a, int b) {
    return a < b ? a : b;
}

int nthUglyNumber(int n) {
    int* ugly = (int*)malloc((size_t)n * sizeof(int));
    ugly[0] = 1;
    int index2 = 0;
    int index3 = 0;
    int index5 = 0;
    int size = 1;
    while (size < n) {
        int nextUgly = min_int(
            ugly[index2] * 2,
            min_int(ugly[index3] * 3, ugly[index5] * 5)
        );
        ugly[size++] = nextUgly;
        if (nextUgly == ugly[index2] * 2) {
            index2++;
        }
        if (nextUgly == ugly[index3] * 3) {
            index3++;
        }
        if (nextUgly == ugly[index5] * 5) {
            index5++;
        }
    }
    int result = ugly[n - 1];
    free(ugly);
    return result;
}
