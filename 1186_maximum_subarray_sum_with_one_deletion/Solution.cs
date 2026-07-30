// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

using System;

public class Solution {
    public int MaximumSum(int[] arr) {
        int keep = arr[0], delete = arr[0], ans = arr[0];
        for (int i = 1; i < arr.Length; i++) {
            int x = arr[i];
            delete = Math.Max(keep, delete + x);
            keep = Math.Max(keep + x, x);
            ans = Math.Max(ans, Math.Max(keep, delete));
        }
        return ans;
    }
}
