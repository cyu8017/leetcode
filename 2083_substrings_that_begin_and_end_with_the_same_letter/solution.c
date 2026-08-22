// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

#include <string.h>

long long numberOfSubstrings(char* s) {
    long long freq[26] = {0}, ans = 0;
    for (int i = 0; s[i]; i++) {
        freq[s[i] - 'a']++;
        ans += freq[s[i] - 'a'];
    }
    return ans;
}
