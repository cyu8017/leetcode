// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

#include <string.h>

int countLetters(char* s) {
    int n = (int)strlen(s);
    if (n == 0) return 0;
    int ans = 1;
    int length = 1;
    for (int i = 1; i < n; i++) {
        length = (s[i] == s[i - 1]) ? length + 1 : 1;
        ans += length;
    }
    return ans;
}
