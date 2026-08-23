// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

using System;

public class Solution {
    public long CountOperationsToEmptyArray(int[] nums) {
        int n = nums.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => nums[a].CompareTo(nums[b]));
        long ans = n;
        for (int i = 1; i < n; i++)
            if (idx[i] < idx[i - 1]) ans += n - i;
        return ans;
    }
}
