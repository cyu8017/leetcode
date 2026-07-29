// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

#include <stdbool.h>
#include <string.h>

bool canConstruct(char* s, int k) {
    int n = (int)strlen(s);
    if (k > n) return false;
    int cnt[26] = {0};
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    int odd = 0;
    for (int i = 0; i < 26; i++) odd += cnt[i] % 2;
    return odd <= k;
}
