// LeetCode 1375 - Number Of Times Binary String Is Prefix Aligned
// https://leetcode.com/problems/number-of-times-binary-String-is-prefix-aligned/

class Solution {
    public int numTimesAllBlue(int[] flips) {
        int ans = 0, mx = 0;
        for (int i = 0; i < flips.length; i++) {
            mx = Math.max(mx, flips[i]);
            if (mx == i + 1) ans++;
        }
        return ans;
    }
}
