// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution {
    private int ans, maxOr;
    private int[] nums;

    public int countMaxOrSubsets(int[] nums) {
        this.nums = nums;
        maxOr = 0; ans = 0;
        for (int x : nums) maxOr |= x;
        dfs(0, 0);
        return ans;
    }

    private void dfs(int i, int cur) {
        if (i == nums.length) { if (cur == maxOr) ans++; return; }
        dfs(i + 1, cur);
        dfs(i + 1, cur | nums[i]);
    }
}
