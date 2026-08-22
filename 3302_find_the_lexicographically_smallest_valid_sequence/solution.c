// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool canFinish(char* w1, char* w2, int i, int j, bool usedSkip, int* right, int n, int m) {
    if (j >= m) return true;
    if (!usedSkip) {
        if (right[j] >= i) return true;
        if (j + 1 <= m && right[j + 1] > i) return true;
        if (right[j] > i) return true;
        return false;
    }
    return right[j] >= i;
}

int* validSequence(char* word1, char* word2, int* returnSize) {
    int n = (int)strlen(word1), m = (int)strlen(word2);
    int* right = (int*)malloc((size_t)(m + 1) * sizeof(int));
    right[m] = n;
    int j = m - 1;
    for (int i = n - 1; i >= 0 && j >= 0; i--) {
        if (word1[i] == word2[j]) { right[j] = i; j--; }
    }
    for (; j >= 0; j--) right[j] = -1;
    int* ans = (int*)malloc((size_t)m * sizeof(int));
    bool usedSkip = false;
    int i = 0;
    for (j = 0; j < m; j++) {
        bool found = false;
        while (i < n) {
            if (word1[i] == word2[j]) {
                if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right, n, m)) {
                    ans[j] = i; i++; found = true; break;
                }
            } else if (!usedSkip) {
                if (canFinish(word1, word2, i + 1, j + 1, true, right, n, m)) {
                    ans[j] = i; i++; usedSkip = true; found = true; break;
                }
            }
            i++;
        }
        if (!found) {
            free(ans); free(right);
            *returnSize = 0;
            return (int*)malloc(sizeof(int)); /* empty */
        }
    }
    free(right);
    *returnSize = m;
    return ans;
}
