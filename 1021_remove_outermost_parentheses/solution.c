// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

#include <stdlib.h>
#include <string.h>

char* removeOuterParentheses(char* s) {
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)n + 1);
    int depth = 0, len = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            if (depth) ans[len++] = s[i];
            depth++;
        } else {
            depth--;
            if (depth) ans[len++] = s[i];
        }
    }
    ans[len] = '\0';
    return ans;
}
