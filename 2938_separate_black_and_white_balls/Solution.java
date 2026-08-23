// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

class Solution {
    public long minimumSteps(String s) {
        long ans = 0, zeros = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '0') zeros++;
            else ans += zeros;
        }
        return ans;
    }
}
