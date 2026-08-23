// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

public class Solution {
    int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
    int Lcm(int a, int b) { return a / Gcd(a, b) * b; }

    public long MaxScore(int[] nums) {
        int n = nums.Length;
        int gcdAll = nums[0], lcmAll = nums[0];
        for (int i = 1; i < n; i++) {
            gcdAll = Gcd(gcdAll, nums[i]);
            lcmAll = Lcm(lcmAll, nums[i]);
        }
        long ans = (long)gcdAll * lcmAll;
        for (int skip = 0; skip < n; skip++) {
            int g = 0, l = 1;
            bool first = true;
            for (int i = 0; i < n; i++) {
                if (i == skip) continue;
                if (first) { g = l = nums[i]; first = false; }
                else { g = Gcd(g, nums[i]); l = Lcm(l, nums[i]); }
            }
            if (first) continue;
            long v = (long)g * l;
            if (v > ans) ans = v;
        }
        return ans;
    }
}
