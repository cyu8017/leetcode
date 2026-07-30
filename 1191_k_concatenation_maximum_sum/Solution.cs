// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

using System;
using System.Linq;

public class Solution {
    private const int Mod = 1_000_000_007;

    public int KConcatenationMaxSum(int[] arr, int k) {
        int Kadane(int[] nums) {
            int best = 0, cur = 0;
            foreach (int x in nums) {
                cur = Math.Max(0, cur + x);
                best = Math.Max(best, cur);
            }
            return best;
        }

        int one = Kadane(arr);
        if (k == 1) return one % Mod;
        int two = Kadane(arr.Concat(arr).ToArray());
        long total = arr.Sum(x => (long)x);
        if (total > 0) return (int)Math.Max(one, two + total * (k - 2)) % Mod;
        return Math.Max(one, two) % Mod;
    }
}
