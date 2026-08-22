// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool* transformStr(char* s, char** strs, int strsSize, int* returnSize) {
    int n = (int)strlen(s);
    int* prefix = (int*)malloc((size_t)(n + 1) * sizeof(int));
    prefix[0] = 0;
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (s[i] == '1' ? 1 : 0);
    bool* result = (bool*)malloc((size_t)strsSize * sizeof(bool));
    for (int i = 0; i < strsSize; i++) {
        int left = 0, right = 0;
        int ok = 1;
        for (int j = 0; j < n; j++) {
            left += (strs[i][j] == '1' ? 1 : 0);
            int add = (strs[i][j] != '0' ? 1 : 0);
            right = right + add;
            if (right > prefix[j + 1]) right = prefix[j + 1];
            if (left > right) { ok = 0; break; }
        }
        result[i] = ok && left <= prefix[n] && prefix[n] <= right;
    }
    free(prefix);
    *returnSize = strsSize;
    return result;
}
