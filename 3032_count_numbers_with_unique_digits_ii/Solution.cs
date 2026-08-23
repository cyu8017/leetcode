// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

public class Solution {
    public int NumberCount(int a, int b) {
        string num = b.ToString();
        int[][] f = null;
        void Reset() {
            f = new int[num.Length][];
            for (int i = 0; i < num.Length; i++) {
                f[i] = new int[1 << 10];
                for (int j = 0; j < (1 << 10); j++) f[i][j] = -1;
            }
        }
        Reset();
        int Dfs(int pos, int mask, bool limit) {
            if (pos >= num.Length) return mask != 0 ? 1 : 0;
            if (!limit && f[pos][mask] != -1) return f[pos][mask];
            int up = limit ? num[pos] - '0' : 9;
            int ans = 0;
            for (int i = 0; i <= up; i++) {
                if (((mask >> i) & 1) != 0) continue;
                int nxt = mask | (1 << i);
                if (mask == 0 && i == 0) nxt = 0;
                ans += Dfs(pos + 1, nxt, limit && i == up);
            }
            if (!limit) f[pos][mask] = ans;
            return ans;
        }
        int y = Dfs(0, 0, true);
        num = (a - 1).ToString();
        Reset();
        int x = Dfs(0, 0, true);
        return y - x;
    }
}
