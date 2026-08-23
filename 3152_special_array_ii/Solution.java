// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] d = new int[n];
        for (int i = 0; i < n; i++) d[i] = i;
        for (int i = 1; i < n; i++) {
            if (nums[i] % 2 != nums[i - 1] % 2) d[i] = d[i - 1];
        }
        boolean[] ans = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++)
            ans[i] = d[queries[i][1]] <= queries[i][0];
        return ans;
    }
}
