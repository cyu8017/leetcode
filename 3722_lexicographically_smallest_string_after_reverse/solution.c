// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

#include <stdlib.h>
#include <string.h>

static void reverseRange(char* t, int l, int r) {
    while (l < r) { char c = t[l]; t[l] = t[r]; t[r] = c; l++; r--; }
}

char* lexSmallest(char* s) {
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)(n + 1));
    strcpy(ans, s);
    char* t = (char*)malloc((size_t)(n + 1));
    for (int k = 1; k <= n; k++) {
        strcpy(t, s);
        reverseRange(t, 0, k - 1);
        if (strcmp(t, ans) < 0) strcpy(ans, t);
        strcpy(t, s);
        reverseRange(t, n - k, n - 1);
        if (strcmp(t, ans) < 0) strcpy(ans, t);
    }
    free(t);
    return ans;
}
