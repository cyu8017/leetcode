// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

using System.Collections.Generic;
using System.Numerics;

public class Solution {
    int Depth(long x) {
        if (x == 1) return 0;
        int d = 0;
        while (x > 1) {
            x = BitOperations.PopCount((ulong)x);
            d++;
        }
        return d;
    }

    public int[] PopcountDepth(long[] nums, long[][] queries) {
        long[] a = (long[])nums.Clone();
        var ans = new List<int>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int l = (int)q[1], r = (int)q[2], k = (int)q[3], cnt = 0;
                for (int i = l; i <= r; i++)
                    if (Depth(a[i]) == k) cnt++;
                ans.Add(cnt);
            } else {
                a[(int)q[1]] = q[2];
            }
        }
        return ans.ToArray();
    }
}
