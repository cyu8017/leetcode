// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

#include <stdbool.h>
#include <string.h>

int numberOfSpecialChars(char* word) {
    bool s[128] = {0};
    for (int i = 0; word[i]; i++) s[(unsigned char)word[i]] = true;
    int ans = 0;
    for (int i = 0; i < 26; i++)
        if (s['a' + i] && s['A' + i]) ans++;
    return ans;
}
