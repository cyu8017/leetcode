// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

#include <stdlib.h>
#include <string.h>

char** buildArray(int* target, int targetSize, int n, int* returnSize) {
    (void)n;
    char** ans = (char**)malloc(targetSize * 2 * sizeof(char*));
    int an = 0, current = 1;
    for (int t = 0; t < targetSize; t++) {
        while (current < target[t]) {
            ans[an] = (char*)malloc(5); strcpy(ans[an++], "Push");
            ans[an] = (char*)malloc(4); strcpy(ans[an++], "Pop");
            current++;
        }
        ans[an] = (char*)malloc(5); strcpy(ans[an++], "Push");
        current++;
    }
    *returnSize = an;
    return ans;
}
