// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int* goodIndices(char* s, int* returnSize) {
    int n = (int)strlen(s);
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int asz = 0;
    for (int i = 0; i < n; i++) {
        char t[16];
        sprintf(t, "%d", i);
        int k = (int)strlen(t);
        if (i + 1 - k < 0) continue;
        if (strncmp(s + i + 1 - k, t, (size_t)k) == 0) ans[asz++] = i;
    }
    *returnSize = asz;
    return ans;
}
