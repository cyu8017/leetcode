// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumLength(int[] nums) {
        var cnt = new Dictionary<long, int>();
        foreach (int x in nums) {
            cnt.TryGetValue(x, out int c);
            cnt[x] = c + 1;
        }
        cnt.TryGetValue(1, out int ones);
        int ans = ones - ((ones % 2) ^ 1);
        cnt.Remove(1);
        var keys = new List<long>(cnt.Keys);
        foreach (long start in keys) {
            long x = start;
            int t = 0;
            while (cnt.TryGetValue(x, out int cx) && cx > 1) {
                x = x * x;
                t += 2;
            }
            if (cnt.TryGetValue(x, out int cx2) && cx2 > 0) t += 1;
            else t -= 1;
            ans = Math.Max(ans, t);
        }
        return ans;
    }
}
