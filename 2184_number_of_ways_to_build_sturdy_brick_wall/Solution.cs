// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

public class Solution {
    public int BuildWall(int height, int width, int[] bricks) {
        const int MOD = 1000000007;
        var masks = new List<int>();
        void Gen(int remain, int mask) {
            if (remain == 0) { masks.Add(mask); return; }
            foreach (int b in bricks) {
                if (b <= remain) {
                    int nm = mask;
                    if (remain - b > 0) nm |= 1 << (remain - b);
                    Gen(remain - b, nm);
                }
            }
        }
        Gen(width, 0);
        int m = masks.Count;
        var compat = new List<int>[m];
        for (int i = 0; i < m; i++) {
            compat[i] = new List<int>();
            for (int j = 0; j < m; j++)
                if ((masks[i] & masks[j]) == 0) compat[i].Add(j);
        }
        int[] dp = new int[m];
        Array.Fill(dp, 1);
        for (int h = 1; h < height; h++) {
            int[] ndp = new int[m];
            for (int i = 0; i < m; i++)
                foreach (int j in compat[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
            dp = ndp;
        }
        int ans = 0;
        foreach (int v in dp) ans = (ans + v) % MOD;
        return ans;
    }
}
