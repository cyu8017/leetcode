// LeetCode 0014 - Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

#include <stdlib.h>
#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        char* result = (char*)malloc(1);
        result[0] = '\0';
        return result;
    }

    for (int i = 0; strs[0][i] != '\0'; i++) {
        char ch = strs[0][i];
        for (int j = 1; j < strsSize; j++) {
            if (strs[j][i] == '\0' || strs[j][i] != ch) {
                char* result = (char*)malloc((size_t)i + 1);
                memcpy(result, strs[0], (size_t)i);
                result[i] = '\0';
                return result;
            }
        }
    }

    size_t len = strlen(strs[0]);
    char* result = (char*)malloc(len + 1);
    memcpy(result, strs[0], len + 1);
    return result;
}
