// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

using System.Collections.Generic;

public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        int n = nums.Length;
        int inv = 0, ans = 0;
        var sl = new SortedSet<(int sum, int i)>();
        var idx = new SortedSet<int>();
        for (int i = 0; i < n; i++) idx.Add(i);
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) inv++;
            sl.Add((nums[i] + nums[i + 1], i));
        }
        while (inv > 0) {
            ans++;
            var p = sl.Min;
            sl.Remove(p);
            int s = p.sum, i = p.i;
            int j = idx.GetViewBetween(i + 1, int.MaxValue).Min;
            if (nums[i] > nums[j]) inv--;
            var before = idx.GetViewBetween(int.MinValue, i - 1);
            if (before.Count > 0) {
                int h = before.Max;
                if (nums[h] > nums[i]) inv--;
                sl.Remove((nums[h] + nums[i], h));
                if (nums[h] > s) inv++;
                sl.Add((nums[h] + s, h));
            }
            var after = idx.GetViewBetween(j + 1, int.MaxValue);
            if (after.Count > 0) {
                int k = after.Min;
                if (nums[j] > nums[k]) inv--;
                sl.Remove((nums[j] + nums[k], j));
                if (s > nums[k]) inv++;
                sl.Add((s + nums[k], i));
            }
            nums[i] = s;
            idx.Remove(j);
        }
        return ans;
    }
}
