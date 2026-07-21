// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

#include <stdlib.h>
#include <string.h>

char* replaceDigits(char* s) {
    int n = (int)strlen(s);
    char* result = (char*)malloc((size_t)n + 1);
    strcpy(result, s);
    for (int i = 1; i < n; i += 2) {
        result[i] = (char)(result[i - 1] + (result[i] - '0'));
    }
    return result;
}
