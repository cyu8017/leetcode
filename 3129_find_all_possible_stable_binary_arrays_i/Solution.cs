// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

public class Solution {
    public int NumberOfStableArrays(int zero, int one, int limit) {
        const int Mod = 1000000007;
        int[][][] f = new int[zero + 1][][];
        for (int i = 0; i <= zero; i++) {
            f[i] = new int[one + 1][];
            for (int j = 0; j <= one; j++) f[i][j] = new[] { -1, -1 };
        }
        int Dfs(int i, int j, int k) {
            if (i < 0 || j < 0) return 0;
            if (i == 0) return (k == 1 && j <= limit) ? 1 : 0;
            if (j == 0) return (k == 0 && i <= limit) ? 1 : 0;
            if (f[i][j][k] != -1) return f[i][j][k];
            int res;
            if (k == 0)
                res = (Dfs(i - 1, j, 0) + Dfs(i - 1, j, 1) - Dfs(i - limit - 1, j, 1) + Mod) % Mod;
            else
                res = (Dfs(i, j - 1, 0) + Dfs(i, j - 1, 1) - Dfs(i, j - limit - 1, 0) + Mod) % Mod;
            return f[i][j][k] = res;
        }
        return (Dfs(zero, one, 0) + Dfs(zero, one, 1)) % Mod;
    }
}
