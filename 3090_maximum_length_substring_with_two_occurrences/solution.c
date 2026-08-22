// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

#include <string.h>

int maximumLengthSubstring(char* s) {
    int cnt[26] = {0};
    int l = 0, ans = 0, n = (int)strlen(s);
    for (int r = 0; r < n; r++) {
        int idx = s[r] - 'a';
        cnt[idx]++;
        while (cnt[idx] > 2) { cnt[s[l] - 'a']--; l++; }
        if (r - l + 1 > ans) ans = r - l + 1;
    }
    return ans;
}
