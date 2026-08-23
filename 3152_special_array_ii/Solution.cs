// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

public class Solution {
    public bool[] IsArraySpecial(int[] nums, int[][] queries) {
        int n = nums.Length;
        int[] d = new int[n];
        for (int i = 0; i < n; i++) d[i] = i;
        for (int i = 1; i < n; i++) {
            if (nums[i] % 2 != nums[i - 1] % 2) d[i] = d[i - 1];
        }
        bool[] ans = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++)
            ans[i] = d[queries[i][1]] <= queries[i][0];
        return ans;
    }
}
