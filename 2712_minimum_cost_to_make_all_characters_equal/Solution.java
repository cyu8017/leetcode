// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
    public long minimumCost(String s) {
        int n = s.length();
        long ans = 0;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) != s.charAt(i - 1)) ans += Math.min(i, n - i);
        }
        return ans;
    }
}
