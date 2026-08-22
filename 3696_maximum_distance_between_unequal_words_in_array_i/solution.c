// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

#include <string.h>

int maxDistance(char** words, int wordsSize) {
    int n = wordsSize, ans = 0;
    for (int i = 0; i < n; i++) {
        if (strcmp(words[i], words[0]) != 0) {
            if (i + 1 > ans) ans = i + 1;
        }
        if (strcmp(words[i], words[n - 1]) != 0) {
            if (n - i > ans) ans = n - i;
        }
    }
    return ans;
}
