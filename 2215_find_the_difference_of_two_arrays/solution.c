// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int** findDifference(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize, int** returnColumnSizes) {
    // values in [-1000,1000]
    bool s1[2001] = {0}, s2[2001] = {0};
    for (int i = 0; i < nums1Size; i++) s1[nums1[i] + 1000] = true;
    for (int i = 0; i < nums2Size; i++) s2[nums2[i] + 1000] = true;
    int* a = (int*)malloc(2001 * sizeof(int));
    int* b = (int*)malloc(2001 * sizeof(int));
    int an = 0, bn = 0;
    for (int v = 0; v <= 2000; v++) {
        if (s1[v] && !s2[v]) a[an++] = v - 1000;
        if (s2[v] && !s1[v]) b[bn++] = v - 1000;
    }
    int** ans = (int**)malloc(2 * sizeof(int*));
    ans[0] = a; ans[1] = b;
    *returnColumnSizes = (int*)malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = an;
    (*returnColumnSizes)[1] = bn;
    *returnSize = 2;
    return ans;
}
