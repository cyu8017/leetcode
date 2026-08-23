// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

using System;

public class Solution {
    const int MOD = 1000000007;

    static int Group((int, int) p) {
        if (p.Item2 == 0) return 0;
        if (p.Item1 > 0) return 1;
        return 2;
    }

    public int MaxValue(int[] nums1, int[] nums0) {
        int n = nums1.Length;
        var pairs = new (int, int)[n];
        int b = 0;
        for (int i = 0; i < n; i++) {
            pairs[i] = (nums1[i], nums0[i]);
            b += nums1[i] + nums0[i];
        }
        Array.Sort(pairs, (a, c) => {
            int g1 = Group(a), g2 = Group(c);
            if (g1 != g2) return g1.CompareTo(g2);
            if (g1 == 0) return c.Item1.CompareTo(a.Item1);
            if (g1 == 1) {
                if (a.Item1 != c.Item1) return c.Item1.CompareTo(a.Item1);
                return a.Item2.CompareTo(c.Item2);
            }
            return a.Item2.CompareTo(c.Item2);
        });
        var p = new int[b];
        p[0] = 1;
        for (int i = 1; i < b; i++) p[i] = (int)(2L * p[i - 1] % MOD);
        int ans = 0;
        b--;
        foreach (var pr in pairs) {
            int cnt1 = pr.Item1, cnt0 = pr.Item2;
            while (cnt1 > 0) {
                ans = (ans + p[b]) % MOD;
                b--;
                cnt1--;
            }
            b -= cnt0;
        }
        return ans;
    }
}
