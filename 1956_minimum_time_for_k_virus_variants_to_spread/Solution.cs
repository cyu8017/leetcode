// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

using System;
using System.Linq;

public class Solution {
    public int MinDayskVariants(int[][] points, int k) {
        int ans = int.MaxValue;
        for (int x = 1; x <= 100; x++) {
            for (int y = 1; y <= 100; y++) {
                var dists = points.Select(p => Math.Abs(p[0] - x) + Math.Abs(p[1] - y)).ToArray();
                Array.Sort(dists);
                ans = Math.Min(ans, dists[k - 1]);
            }
        }
        return ans;
    }
}