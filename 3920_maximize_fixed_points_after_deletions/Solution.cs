// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

using System.Collections.Generic;

public class Solution {
    public int MaxFixedPoints(int[] nums) {
        var tails = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (i < nums[i]) continue;
            int d = i - nums[i];
            int idx = tails.BinarySearch(d);
            if (idx < 0) idx = ~idx;
            if (idx == tails.Count) tails.Add(d);
            else tails[idx] = d;
        }
        return tails.Count;
    }
}
