// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

#include <stdlib.h>
#include <string.h>

char* minRemoveToMakeValid(char* s) {
    int n = (int)strlen(s);
    char* chars = (char*)malloc((size_t)n + 1);
    memcpy(chars, s, (size_t)n + 1);
    int* opens = (int*)malloc((size_t)n * sizeof(int));
    int openCount = 0;
    for (int i = 0; i < n; i++) {
        if (chars[i] == '(') opens[openCount++] = i;
        else if (chars[i] == ')') {
            if (openCount) openCount--;
            else chars[i] = '\0';
        }
    }
    for (int i = 0; i < openCount; i++) chars[opens[i]] = '\0';
    free(opens);
    int w = 0;
    for (int i = 0; i < n; i++) {
        if (chars[i]) chars[w++] = chars[i];
    }
    chars[w] = '\0';
    return chars;
}
