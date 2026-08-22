// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

#include <stdlib.h>
#include <string.h>

char* findTheString(int** lcp, int lcpSize, int* lcpColSize) {
    (void)lcpColSize;
    int n = lcpSize;
    char* s = (char*)calloc((size_t)(n + 1), 1);
    char c = 'a';
    for (int i = 0; i < n; i++) {
        if (s[i] != 0) continue;
        if (c > 'z') { free(s); char* empty = (char*)malloc(1); empty[0] = 0; return empty; }
        s[i] = c;
        for (int j = i + 1; j < n; j++) if (lcp[i][j] > 0) s[j] = c;
        c++;
    }
    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int v = 0;
            if (s[i] == s[j]) {
                v = 1;
                if (i + 1 < n && j + 1 < n) v += lcp[i + 1][j + 1];
            }
            if (lcp[i][j] != v) { free(s); char* empty = (char*)malloc(1); empty[0] = 0; return empty; }
        }
    }
    return s;
}
