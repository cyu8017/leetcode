// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

using System.Collections.Generic;
public class Solution {
    public int ConstrainedSubsetSum(int[] nums, int k) {
        var queue = new LinkedList<int>();
        var best = (int[])nums.Clone();
        int ans = nums[0];
        for (int i = 0; i < nums.Length; i++) {
            while (queue.Count > 0 && queue.First.Value < i - k) queue.RemoveFirst();
            best[i] = nums[i] + (queue.Count > 0 ? System.Math.Max(0, best[queue.First.Value]) : 0);
            while (queue.Count > 0 && best[queue.Last.Value] <= best[i]) queue.RemoveLast();
            queue.AddLast(i);
            ans = System.Math.Max(ans, best[i]);
        }
        return ans;
    }
}
