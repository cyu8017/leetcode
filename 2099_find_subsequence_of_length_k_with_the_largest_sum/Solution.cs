// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

public class Solution {
    public int[] MaxSubsequence(int[] nums, int k) {
        var arr = new (int val, int idx)[nums.Length];
        for (int i = 0; i < nums.Length; i++) arr[i] = (nums[i], i);
        Array.Sort(arr, (a, b) => b.val.CompareTo(a.val));
        int[] idx = new int[k];
        for (int i = 0; i < k; i++) idx[i] = arr[i].idx;
        Array.Sort(idx);
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) ans[i] = nums[idx[i]];
        return ans;
    }
}
