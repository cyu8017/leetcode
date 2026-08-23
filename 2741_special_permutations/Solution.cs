// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

public class Solution {
    public int SpecialPerm(int[] nums) {
        const int MOD = 1000000007;
        int n = nums.Length;
        int[,] memo = new int[1 << n, n];
        for (int i = 0; i < (1 << n); i++)
            for (int j = 0; j < n; j++) memo[i, j] = -1;
        int Dfs(int mask, int last) {
            if (mask == (1 << n) - 1) return 1;
            if (memo[mask, last] != -1) return memo[mask, last];
            int res = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                if (nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0)
                    res = (res + Dfs(mask | (1 << i), i)) % MOD;
            }
            return memo[mask, last] = res;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) ans = (ans + Dfs(1 << i, i)) % MOD;
        return ans;
    }
}
