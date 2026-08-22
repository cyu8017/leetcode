// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

#include <string.h>

int numberOfSpecialSubstrings(char* s) {
    int last[26];
    for (int i = 0; i < 26; i++) last[i] = -1;
    int ans = 0, left = 0, n = (int)strlen(s);
    for (int right = 0; right < n; right++) {
        int c = s[right] - 'a';
        if (last[c] >= left) left = last[c] + 1;
        last[c] = right;
        ans += right - left + 1;
    }
    return ans;
}
