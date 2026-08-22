// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

#include <stdlib.h>
#include <string.h>

char* reverseParentheses(char* s) {
    int n = (int)strlen(s);
    char* stack = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == ')') {
            char* chunk = (char*)malloc((size_t)n + 1);
            int clen = 0;
            while (top > 0 && stack[top - 1] != '(') {
                chunk[clen++] = stack[--top];
            }
            if (top > 0) top--;
            for (int j = 0; j < clen; j++) stack[top++] = chunk[j];
            free(chunk);
        } else {
            stack[top++] = s[i];
        }
    }
    stack[top] = '\0';
    char* ans = (char*)malloc((size_t)top + 1);
    memcpy(ans, stack, (size_t)top + 1);
    free(stack);
    return ans;
}
