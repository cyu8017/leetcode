// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

int longestContinuousSubstring(char* s) {
    int ans = 1, cur = 1;
    for (int i = 1; s[i]; i++) {
        if (s[i] == s[i - 1] + 1) { cur++; if (cur > ans) ans = cur; }
        else cur = 1;
    }
    return ans;
}
