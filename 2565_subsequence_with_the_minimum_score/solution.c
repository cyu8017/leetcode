// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

#include <stdlib.h>
#include <string.h>

int minimumScore(char* s, char* t) {
    int n = (int)strlen(s), m = (int)strlen(t);
    int* left = (int*)malloc((size_t)m * sizeof(int));
    int* right = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) { left[i] = -1; right[i] = -1; }
    int j = 0;
    for (int i = 0; i < n && j < m; i++) {
        if (s[i] == t[j]) { left[j] = i; j++; }
    }
    j = m - 1;
    for (int i = n - 1; i >= 0 && j >= 0; i--) {
        if (s[i] == t[j]) { right[j] = i; j--; }
    }
    if (left[m - 1] != -1) { free(left); free(right); return 0; }
    int ans = m;
    for (int i = 0; i < m; i++) {
        if (right[i] != -1) { if (i < ans) ans = i; break; }
    }
    for (int i = m - 1; i >= 0; i--) {
        if (left[i] != -1) { if (m - 1 - i < ans) ans = m - 1 - i; break; }
    }
    j = 0;
    for (int i = 0; i < m; i++) {
        if (left[i] == -1) break;
        while (j < m && (right[j] == -1 || right[j] <= left[i])) j++;
        if (j < m) {
            int rem = j - i - 1;
            if (rem < ans) ans = rem;
        }
    }
    free(left); free(right);
    return ans;
}
