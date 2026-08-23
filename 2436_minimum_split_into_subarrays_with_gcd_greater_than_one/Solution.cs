// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

public class Solution {
    public int MinimumSplits(int[] nums) {
        int ans = 1;
        int g = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            int ng = Gcd(g, nums[i]);
            if (ng == 1) {
                ans++;
                g = nums[i];
            } else {
                g = ng;
            }
        }
        return ans;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
