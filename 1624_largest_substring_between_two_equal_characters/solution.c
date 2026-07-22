// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

#include <string.h>

int maxLengthBetweenEqualCharacters(char* s) {
    int first[26];
    for (int i = 0; i < 26; i++) first[i] = -1;
    int ans = -1;
    for (int i = 0; s[i]; i++) {
        int c = s[i] - 'a';
        if (first[c] < 0) first[c] = i;
        else if (i - first[c] - 1 > ans) ans = i - first[c] - 1;
    }
    return ans;
}
