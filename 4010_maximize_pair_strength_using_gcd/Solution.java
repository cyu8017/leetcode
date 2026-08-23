// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

class Solution {
    static long Gcd(long a, long b) {
        while (b != 0) { long t = a % b; a = b; b = t; }
        return a;
    }

    public long maxPairStrength(int[] nums) {
        int n = nums.length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long g = Gcd(nums[i], nums[j]);
                long x = (long)nums[i] * nums[j] / (g * g);
                ans = Math.max(ans, x);
            }
        }
        return ans;
    }
}
