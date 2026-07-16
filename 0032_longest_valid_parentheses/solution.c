// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

#include <stdlib.h>
#include <string.h>

int longestValidParentheses(char* s) {
    int len = (int)strlen(s);
    int* stack = (int*)malloc((size_t)(len + 1) * sizeof(int));
    int top = 0;
    stack[top++] = -1;
    int best = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            stack[top++] = i;
        } else {
            top--;
            if (top == 0) {
                stack[top++] = i;
            } else {
                int span = i - stack[top - 1];
                if (span > best) {
                    best = span;
                }
            }
        }
    }

    free(stack);
    return best;
}
