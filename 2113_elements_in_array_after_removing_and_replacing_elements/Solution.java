// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

class Solution {
    public int[] elementInNums(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int t = queries[i][0], idx = queries[i][1];
            int cycle = t % (2 * n);
            int size, offset;
            if (cycle < n) {
                size = n - cycle;
                offset = cycle;
            } else {
                size = cycle - n;
                offset = 0;
            }
            ans[i] = idx >= size ? -1 : nums[offset + idx];
        }
        return ans;
    }
}
