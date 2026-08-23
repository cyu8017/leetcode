// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

using System;

public class Solution {
    public long FindScore(int[] nums) {
        int n = nums.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; ++i) idx[i] = i;
        Array.Sort(idx, (a, b) => {
            if (nums[a] != nums[b]) return nums[a].CompareTo(nums[b]);
            return a.CompareTo(b);
        });
        bool[] marked = new bool[n];
        long ans = 0;
        foreach (int i in idx) {
            if (marked[i]) continue;
            ans += nums[i];
            marked[i] = true;
            if (i > 0) marked[i - 1] = true;
            if (i + 1 < n) marked[i + 1] = true;
        }
        return ans;
    }
}
