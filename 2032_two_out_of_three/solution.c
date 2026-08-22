// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

#include <stdlib.h>
#include <string.h>

int* twoOutOfThree(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* returnSize) {
    int seen[3][101];
    memset(seen, 0, sizeof(seen));
    for (int i = 0; i < nums1Size; i++) seen[0][nums1[i]] = 1;
    for (int i = 0; i < nums2Size; i++) seen[1][nums2[i]] = 1;
    for (int i = 0; i < nums3Size; i++) seen[2][nums3[i]] = 1;
    int* ans = (int*)malloc(100 * sizeof(int));
    int n = 0;
    for (int v = 1; v <= 100; v++) {
        int c = seen[0][v] + seen[1][v] + seen[2][v];
        if (c >= 2) ans[n++] = v;
    }
    *returnSize = n;
    return ans;
}
