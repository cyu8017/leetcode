// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

#include <stdlib.h>

int* stableMountains(int* height, int heightSize, int threshold, int* returnSize) {
    int* ans = (int*)malloc((size_t)heightSize * sizeof(int));
    int n = 0;
    for (int i = 1; i < heightSize; i++) {
        if (height[i - 1] > threshold) ans[n++] = i;
    }
    *returnSize = n;
    return ans;
}
