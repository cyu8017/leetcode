// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

#include <string.h>

int findLUSlength(char* a, char* b) {
    if (strcmp(a, b) != 0) {
        const int lengthA = (int)strlen(a);
        const int lengthB = (int)strlen(b);
        return lengthA > lengthB ? lengthA : lengthB;
    }
    return -1;
}
