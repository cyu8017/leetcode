// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

class Solution {
    private int[] nums;
    private int[] f;
    private int n;

    public int maxScore(int[] nums) {
        this.nums = nums;
        n = nums.length;
        f = new int[n];
        return dfs(0);
    }

    private int dfs(int i) {
        if (f[i] > 0) {
            return f[i];
        }
        for (int j = i + 1; j < n; j++) {
            f[i] = Math.max(f[i], (j - i) * nums[j] + dfs(j));
        }
        return f[i];
    }
}
