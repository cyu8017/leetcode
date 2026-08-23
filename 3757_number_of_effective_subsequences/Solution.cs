// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

using System.Collections.Generic;

public class Solution {
    static int PopCount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public int CountEffectiveSubsequences(int[] nums) {
        const int mod = 1000000007;
        int all = 0;
        foreach (int x in nums) all |= x;
        var bits = new List<int>();
        for (int b = 0; b < 20; b++) if (((all >> b) & 1) != 0) bits.Add(b);
        int m = bits.Count;
        int[] freq = new int[1 << m];
        foreach (int x in nums) {
            int mask = 0;
            for (int i = 0; i < m; i++) if (((x >> bits[i]) & 1) != 0) mask |= 1 << i;
            freq[mask]++;
        }
        int[] disjoint = (int[])freq.Clone();
        for (int b = 0; b < m; b++) {
            for (int mask = 0; mask < (1 << m); mask++) {
                if (((mask >> b) & 1) != 0) disjoint[mask] += disjoint[mask ^ (1 << b)];
            }
        }
        int[] pow2 = new int[nums.Length + 1];
        pow2[0] = 1;
        for (int i = 1; i <= nums.Length; i++) pow2[i] = pow2[i - 1] * 2 % mod;
        int ans = 0, full = (1 << m) - 1;
        for (int s = 1; s <= full; s++) {
            int ways = pow2[disjoint[full ^ s]];
            int bc = PopCount(s);
            if ((bc & 1) != 0) {
                ans += ways;
                if (ans >= mod) ans -= mod;
            } else {
                ans -= ways;
                if (ans < 0) ans += mod;
            }
        }
        return ans;
    }
}
