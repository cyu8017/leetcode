// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

using System;

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public long GcdSum(int[] nums) {
        int n = nums.Length;
        var prefixGcd = new int[n];
        int mx = 0;
        for (int i = 0; i < n; i++) {
            mx = Math.Max(mx, nums[i]);
            prefixGcd[i] = Gcd(nums[i], mx);
        }
        Array.Sort(prefixGcd);
        long ans = 0;
        for (int i = 0; i < n / 2; i++) ans += Gcd(prefixGcd[i], prefixGcd[n - i - 1]);
        return ans;
    }
}
