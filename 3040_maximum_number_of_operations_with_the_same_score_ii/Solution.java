// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution {
    private int[] nums;
    private int[][] f;
    private int s;

    private int dfs(int i, int j) {
        if (j - i < 1) return 0;
        if (f[i][j] != -1) return f[i][j];
        int ans = 0;
        if (nums[i] + nums[i + 1] == s) ans = Math.max(ans, 1 + dfs(i + 2, j));
        if (nums[i] + nums[j] == s) ans = Math.max(ans, 1 + dfs(i + 1, j - 1));
        if (nums[j - 1] + nums[j] == s) ans = Math.max(ans, 1 + dfs(i, j - 2));
        return f[i][j] = ans;
    }

    private int g(int i0, int j0, int score) {
        int n = nums.length;
        f = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) f[i][j] = -1;
        s = score;
        return dfs(i0, j0);
    }

    public int maxOperations(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        int a = g(2, n - 1, nums[0] + nums[1]);
        int b = g(0, n - 3, nums[n - 1] + nums[n - 2]);
        int c = g(1, n - 2, nums[0] + nums[n - 1]);
        return 1 + Math.max(a, Math.max(b, c));
    }
}
