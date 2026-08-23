// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

class Solution {
    public long maximumSumScore(int[] nums) {
        long total = 0, pref = 0;
        for (int x : nums) total += x;
        long ans = Long.MIN_VALUE;
        for (int x : nums) {
            pref += x;
            ans = Math.max(ans, Math.max(pref, total - pref + x));
        }
        return ans;
    }
}
