// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

using System.Collections.Generic;

public class Solution {
    public IList<int> GetGoodIndices(int[][] variables, int target) {
        long ModPow(long a, long b, long mod) {
            long res = 1 % mod;
            a %= mod;
            while (b > 0) {
                if ((b & 1) != 0) res = res * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return res;
        }
        var ans = new List<int>();
        for (int i = 0; i < variables.Length; i++) {
            var v = variables[i];
            int a = v[0], b = v[1], c = v[2], m = v[3];
            if (ModPow(ModPow(a, b, 10), c, m) == target) ans.Add(i);
        }
        return ans;
    }
}
