// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

int longestIdealString(char* s, int k) {
    int dp[26] = {0}, ans = 0;
    for (int i = 0; s[i]; i++) {
        int c = s[i] - 'a', best = 0;
        for (int p = 0; p < 26; p++) {
            int diff = c - p; if (diff < 0) diff = -diff;
            if (diff <= k && dp[p] > best) best = dp[p];
        }
        dp[c] = best + 1;
        if (dp[c] > ans) ans = dp[c];
    }
    return ans;
}
