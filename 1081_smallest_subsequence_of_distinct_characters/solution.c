// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* smallestSubsequence(char* s) {
    int n = (int)strlen(s);
    int last[26];
    for (int i = 0; i < 26; i++) {
        last[i] = -1;
    }
    for (int i = 0; i < n; i++) {
        last[s[i] - 'a'] = i;
    }
    char* stack = (char*)malloc((size_t)n + 1);
    int top = 0;
    bool used[26] = {false};
    for (int i = 0; i < n; i++) {
        char ch = s[i];
        if (used[ch - 'a']) {
            continue;
        }
        while (top > 0 && ch < stack[top - 1] && last[stack[top - 1] - 'a'] > i) {
            used[stack[--top] - 'a'] = false;
        }
        stack[top++] = ch;
        used[ch - 'a'] = true;
    }
    stack[top] = '\0';
    return stack;
}
