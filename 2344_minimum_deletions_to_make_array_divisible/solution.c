// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

#include <stdlib.h>

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minOperations(int* nums, int numsSize, int* numsDivide, int numsDivideSize) {
    int g = numsDivide[0];
    for (int i = 1; i < numsDivideSize; i++) g = gcd(g, numsDivide[i]);
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    for (int i = 0; i < numsSize; i++) {
        if (g % nums[i] == 0) return i;
    }
    return -1;
}
