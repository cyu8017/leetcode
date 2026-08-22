// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool checkPartitioning(char* s) {
    int n = strlen(s);
    bool* pal = (bool*)calloc((size_t)n * n, sizeof(bool));
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            pal[i * n + j] = s[i] == s[j] && (j - i < 2 || pal[(i + 1) * n + (j - 1)]);
        }
    }
    bool ans = false;
    for (int i = 0; i < n - 2 && !ans; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            if (pal[0 * n + i] && pal[(i + 1) * n + j] && pal[(j + 1) * n + (n - 1)]) {
                ans = true;
                break;
            }
        }
    }
    free(pal);
    return ans;
}
