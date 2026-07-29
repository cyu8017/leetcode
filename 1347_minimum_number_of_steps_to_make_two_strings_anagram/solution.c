// LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

#include <string.h>

int minSteps(char* s, char* t) {
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    for (int i = 0; t[i]; i++) cnt[t[i] - 'a']--;
    int ans = 0;
    for (int i = 0; i < 26; i++) if (cnt[i] > 0) ans += cnt[i];
    return ans;
}
