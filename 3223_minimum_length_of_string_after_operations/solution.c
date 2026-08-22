// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

int minimumLength(char* s) {
    int cnt[26] = {0}, ans = 0;
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    for (int i = 0; i < 26; i++)
        if (cnt[i] > 0) ans += (cnt[i] & 1) ? 1 : 2;
    return ans;
}
