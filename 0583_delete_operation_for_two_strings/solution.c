// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

#include <stdlib.h>
#include <string.h>

int minDistance(char* word1, char* word2) {
    int m = (int)strlen(word1);
    int n = (int)strlen(word2);
    int* prev = (int*)calloc((size_t)n + 1, sizeof(int));
    int* curr = (int*)calloc((size_t)n + 1, sizeof(int));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                curr[j] = prev[j - 1] + 1;
            } else {
                curr[j] = prev[j] > curr[j - 1] ? prev[j] : curr[j - 1];
            }
        }
        int* tmp = prev;
        prev = curr;
        curr = tmp;
        memset(curr, 0, ((size_t)n + 1) * sizeof(int));
    }

    int lcs = prev[n];
    free(prev);
    free(curr);
    return m + n - 2 * lcs;
}
