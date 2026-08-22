// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

#include <stdlib.h>

int* circularPermutation(int n, int start, int* returnSize) {
    int size = 1 << n;
    int* ans = (int*)malloc((size_t)size * sizeof(int));
    for (int i = 0; i < size; i++) ans[i] = start ^ i ^ (i >> 1);
    *returnSize = size;
    return ans;
}
