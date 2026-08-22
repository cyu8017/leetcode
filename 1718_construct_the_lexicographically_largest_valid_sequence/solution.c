// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool backtrack(int i, int n, int size, int* ans, bool* used) {
    while (i < size && ans[i] != 0) {
        i++;
    }
    if (i == size) {
        return true;
    }
    for (int value = n; value >= 1; value--) {
        if (used[value]) {
            continue;
        }
        if (value == 1) {
            ans[i] = 1;
            used[1] = true;
            if (backtrack(i + 1, n, size, ans, used)) {
                return true;
            }
            used[1] = false;
            ans[i] = 0;
        } else {
            int j = i + value;
            if (j < size && ans[j] == 0) {
                ans[i] = value;
                ans[j] = value;
                used[value] = true;
                if (backtrack(i + 1, n, size, ans, used)) {
                    return true;
                }
                used[value] = false;
                ans[i] = 0;
                ans[j] = 0;
            }
        }
    }
    return false;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructDistancedSequence(int n, int* returnSize) {
    int size = 2 * n - 1;
    int* ans = (int*)calloc(size, sizeof(int));
    bool* used = (bool*)calloc(n + 1, sizeof(bool));
    backtrack(0, n, size, ans, used);
    free(used);
    *returnSize = size;
    return ans;
}
