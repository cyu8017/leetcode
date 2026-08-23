// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

class Solution {
    public int minOperations(String s) {
        int ans = 0;
        for (char c : s.toCharArray()) {
            if (c != 'a') ans = Math.max(ans, 26 - (c - 'a'));
        }
        return ans;
    }
}
