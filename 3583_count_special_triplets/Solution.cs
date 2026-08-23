// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

using System.Collections.Generic;

public class Solution {
    public int SpecialTriplets(int[] nums) {
        var left = new Dictionary<int, int>();
        var right = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!right.ContainsKey(x)) right[x] = 0;
            right[x]++;
        }
        long ans = 0, mod = 1000000007;
        foreach (int x in nums) {
            right[x]--;
            long lv = left.ContainsKey(x * 2) ? left[x * 2] : 0;
            long rv = right.ContainsKey(x * 2) ? right[x * 2] : 0;
            ans = (ans + lv * rv % mod) % mod;
            if (!left.ContainsKey(x)) left[x] = 0;
            left[x]++;
        }
        return (int)ans;
    }
}
