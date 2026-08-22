// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

int findTheLongestBalancedSubstring(char* s) {
    int ans = 0, zeros = 0, ones = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '0') {
            if (ones > 0) { zeros = 0; ones = 0; }
            zeros++;
        } else {
            ones++;
            int cur = ones < zeros ? ones : zeros;
            if (2 * cur > ans) ans = 2 * cur;
        }
    }
    return ans;
}
