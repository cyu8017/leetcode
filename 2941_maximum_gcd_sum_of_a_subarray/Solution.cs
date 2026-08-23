// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

using System.Collections.Generic;

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public long MaxGcdSum(int[] nums, int k) {
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        long ans = 0;
        var st = new List<(int g, int idx)>();
        for (int i = 0; i < n; i++) {
            var nst = new List<(int g, int idx)> { (nums[i], i) };
            foreach (var (g0, idx) in st) {
                int g = Gcd(g0, nums[i]);
                if (nst[nst.Count - 1].g == g) continue;
                nst.Add((g, idx));
            }
            st = nst;
            foreach (var (g, idx) in st) {
                if (i - idx + 1 >= k) {
                    long cand = (pref[i + 1] - pref[idx]) * g;
                    if (cand > ans) ans = cand;
                }
            }
        }
        return ans;
    }
}
