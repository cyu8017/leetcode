// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

#include <string.h>

int minimumTimeToInitialState(char* word, int k) {
    int n = (int)strlen(word);
    for (int i = k; i < n; i += k) {
        if (strncmp(word + i, word, n - i) == 0) return i / k;
    }
    return (n + k - 1) / k;
}
