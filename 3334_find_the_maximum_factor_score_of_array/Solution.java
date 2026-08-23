// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
    private int lcm(int a, int b) { return a / gcd(a, b) * b; }

    public long maxScore(int[] nums) {
        int n = nums.length;
        int gcdAll = nums[0], lcmAll = nums[0];
        for (int i = 1; i < n; i++) {
            gcdAll = gcd(gcdAll, nums[i]);
            lcmAll = lcm(lcmAll, nums[i]);
        }
        long ans = (long) gcdAll * lcmAll;
        for (int skip = 0; skip < n; skip++) {
            int g = 0, l = 1;
            boolean first = true;
            for (int i = 0; i < n; i++) {
                if (i == skip) continue;
                if (first) { g = l = nums[i]; first = false; }
                else { g = gcd(g, nums[i]); l = lcm(l, nums[i]); }
            }
            if (first) continue;
            long v = (long) g * l;
            if (v > ans) ans = v;
        }
        return ans;
    }
}
