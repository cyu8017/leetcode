// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

public class Solution {
    public int MaximumGood(int[][] statements) {
        int n = statements.Length, ans = 0;
        bool Ok(int mask) {
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) continue;
                for (int j = 0; j < n; j++) {
                    int s = statements[i][j];
                    if (s == 2) continue;
                    bool goodJ = (mask & (1 << j)) != 0;
                    if ((s == 1 && !goodJ) || (s == 0 && goodJ)) return false;
                }
            }
            return true;
        }
        for (int mask = 0; mask < (1 << n); mask++)
            if (Ok(mask)) ans = Math.Max(ans, System.Numerics.BitOperations.PopCount((uint)mask));
        return ans;
    }
}
