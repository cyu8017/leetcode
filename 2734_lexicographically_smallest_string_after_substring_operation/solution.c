// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

#include <stdlib.h>
#include <string.h>

char* smallestString(char* s) {
    int n = (int)strlen(s);
    char* b = (char*)malloc((size_t)n + 1);
    memcpy(b, s, (size_t)n + 1);
    int i = 0;
    while (i < n && b[i] == 'a') i++;
    if (i == n) {
        b[n - 1] = 'z';
        return b;
    }
    while (i < n && b[i] != 'a') {
        b[i]--;
        i++;
    }
    return b;
}
