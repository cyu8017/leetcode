// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

int maxDistinct(char* s) {
    int cnt[26] = {0}, ans = 0;
    for (int i = 0; s[i]; i++) {
        cnt[s[i] - 'a']++;
        if (cnt[s[i] - 'a'] == 1) ans++;
    }
    return ans;
}
