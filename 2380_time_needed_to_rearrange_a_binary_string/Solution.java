// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

class Solution {
    public int secondsToRemoveOccurrences(String s) {
        int ans = 0, zeros = 0;
        for (char c : s) {
            if (c == '0') zeros++;
            else if (zeros > 0) ans = Math.max(ans + 1, zeros);
        }
        return ans;
    }
}
