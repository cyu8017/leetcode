// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSum(int[] nums) {
        var best = new Dictionary<int, int>();
        int ans = -1;
        foreach (int v in nums) {
            int x = v, md = 0;
            while (x > 0) { md = Math.Max(md, x % 10); x /= 10; }
            if (best.ContainsKey(md)) {
                ans = Math.Max(ans, best[md] + v);
                best[md] = Math.Max(best[md], v);
            } else best[md] = v;
        }
        return ans;
    }
}
