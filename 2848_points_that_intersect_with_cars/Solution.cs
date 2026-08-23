// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

using System.Collections.Generic;

public class Solution {
    public int NumberOfPoints(IList<IList<int>> nums) {
        int[] cov = new int[102];
        foreach (var r in nums)
            for (int x = r[0]; x <= r[1]; x++) cov[x] = 1;
        int ans = 0;
        foreach (int v in cov) ans += v;
        return ans;
    }
}
