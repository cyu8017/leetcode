// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool repeatedSubstringPattern(char* s) {
    int n = (int)strlen(s);
    if (n <= 1) {
        return false;
    }
    char* doubled = (char*)malloc((size_t)n * 2 + 1);
    memcpy(doubled, s, (size_t)n);
    memcpy(doubled + n, s, (size_t)n);
    doubled[n * 2] = '\0';
    bool found = false;
    for (int i = 1; i < n; i++) {
        if (strncmp(doubled + i, s, (size_t)n) == 0) {
            found = true;
            break;
        }
    }
    free(doubled);
    return found;
}
