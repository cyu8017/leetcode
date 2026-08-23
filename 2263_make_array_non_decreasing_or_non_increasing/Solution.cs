// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

using System;
using System.Collections.Generic;

public class Solution {
    public int ConvertArray(int[] nums) {
        int Cost(IList<int> arr) {
            var h = new PriorityQueue<int, int>();
            int ans = 0;
            foreach (int x in arr) {
                if (h.Count > 0) {
                    h.TryPeek(out int top, out _);
                    if (top > x) {
                        h.TryDequeue(out int t, out _);
                        ans += t - x;
                        h.Enqueue(x, -x);
                    }
                }
                h.Enqueue(x, -x);
            }
            return ans;
        }
        var rev = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) rev[i] = nums[nums.Length - 1 - i];
        return Math.Min(Cost(nums), Cost(rev));
    }
}
