// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

#include <stdlib.h>

long long* sumOfThree(long long num, int* returnSize) {
    if (num % 3 != 0) { *returnSize = 0; return NULL; }
    long long* ans = (long long*)malloc(3 * sizeof(long long));
    long long x = num / 3;
    ans[0] = x - 1; ans[1] = x; ans[2] = x + 1;
    *returnSize = 3;
    return ans;
}
