// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

using System.Collections.Generic;

public class Solution {
    public int CountSequences(int[] nums, long k) {
        int n = nums.Length;
        var f = new Dictionary<(int, long, long), int>();
        long Gcd(long a, long b) {
            while (b != 0) {
                long t = a % b;
                a = b;
                b = t;
            }
            return a;
        }
        int Dfs(int i, long p, long q) {
            if (i == n) return (p == k && q == 1) ? 1 : 0;
            var key = (i, p, q);
            if (f.ContainsKey(key)) return f[key];
            int res = Dfs(i + 1, p, q);
            long x = nums[i];
            long g1 = Gcd(p * x, q);
            res += Dfs(i + 1, (p * x) / g1, q / g1);
            long g2 = Gcd(p, q * x);
            res += Dfs(i + 1, p / g2, (q * x) / g2);
            return f[key] = res;
        }
        return Dfs(0, 1, 1);
    }
}
