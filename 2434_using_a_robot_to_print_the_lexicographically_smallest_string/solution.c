// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

#include <stdlib.h>
#include <string.h>

char* robotWithString(char* s) {
    int n = (int)strlen(s);
    char* minSuf = (char*)malloc((size_t)(n + 1));
    minSuf[n] = 'z' + 1;
    for (int i = n - 1; i >= 0; i--) {
        minSuf[i] = s[i];
        if (minSuf[i + 1] < minSuf[i]) minSuf[i] = minSuf[i + 1];
    }
    char* stack = (char*)malloc((size_t)(n + 1));
    char* ans = (char*)malloc((size_t)(n + 1));
    int top = 0, ap = 0;
    for (int i = 0; i < n; i++) {
        stack[top++] = s[i];
        while (top > 0 && stack[top - 1] <= minSuf[i + 1]) ans[ap++] = stack[--top];
    }
    while (top > 0) ans[ap++] = stack[--top];
    ans[ap] = '\0';
    free(minSuf); free(stack);
    return ans;
}
