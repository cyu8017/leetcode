// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

#include <stdlib.h>

int* findPeaks(int* mountain, int mountainSize, int* returnSize) {
    int* ans = (int*)malloc(mountainSize * sizeof(int));
    int an = 0;
    for (int i = 1; i + 1 < mountainSize; i++) {
        if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) ans[an++] = i;
    }
    *returnSize = an;
    return ans;
}
