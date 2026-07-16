// LeetCode 0392 - Is Subsequence
// https://leetcode.com/problems/is-subsequence/

#include <stdbool.h>

bool isSubsequence(char* s, char* t) {
    int index = 0;

    for (int tIndex = 0; t[tIndex] != '\0'; tIndex++) {
        if (s[index] != '\0' && s[index] == t[tIndex]) {
            index += 1;
        }
    }

    return s[index] == '\0';
}
