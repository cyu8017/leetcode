// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

#include <stdlib.h>

long long* maximumEvenSplit(long long finalSum, int* returnSize) {
    if (finalSum % 2 != 0) { *returnSize = 0; return NULL; }
    long long* ans = (long long*)malloc(100000 * sizeof(long long));
    int an = 0;
    for (long long x = 2; x <= finalSum; x += 2) {
        ans[an++] = x;
        finalSum -= x;
    }
    ans[an - 1] += finalSum;
    *returnSize = an;
    return ans;
}
