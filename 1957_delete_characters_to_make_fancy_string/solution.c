// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

#include <stdlib.h>
#include <string.h>

char* makeFancyString(char* s) {
    int n = (int)strlen(s);
    char* res = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (top >= 2 && res[top - 1] == s[i] && res[top - 2] == s[i]) continue;
        res[top++] = s[i];
    }
    res[top] = '\0';
    return res;
}
