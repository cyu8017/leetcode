// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

#include <stdlib.h>
#include <string.h>

char** divideString(char* s, int k, char fill, int* returnSize) {
    int n = (int)strlen(s);
    int groups = (n + k - 1) / k;
    char** ans = (char**)malloc((size_t)groups * sizeof(char*));
    for (int g = 0, i = 0; g < groups; g++, i += k) {
        ans[g] = (char*)malloc((size_t)k + 1);
        int len = n - i;
        if (len > k) len = k;
        memcpy(ans[g], s + i, (size_t)len);
        for (int j = len; j < k; j++) ans[g][j] = fill;
        ans[g][k] = '\0';
    }
    *returnSize = groups;
    return ans;
}
