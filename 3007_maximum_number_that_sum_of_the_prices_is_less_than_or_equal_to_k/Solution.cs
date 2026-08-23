// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

public class Solution {
    public long FindMaximumNumber(long k, int x) {
        long l = 1, r = (long)1e17;
        long num = 0;
        long[,] f = new long[65, 65];
        long Dfs(int pos, int cnt, bool limit) {
            if (pos == 0) return cnt;
            if (!limit && f[pos, cnt] != -1) return f[pos, cnt];
            long ans = 0;
            int up = limit ? (int)((num >> (pos - 1)) & 1) : 1;
            for (int i = 0; i <= up; i++) {
                int v = cnt;
                if (i == 1 && pos % x == 0) v++;
                ans += Dfs(pos - 1, v, limit && i == up);
            }
            if (!limit) f[pos, cnt] = ans;
            return ans;
        }
        while (l < r) {
            long mid = (l + r + 1) >> 1;
            num = mid;
            int m = 0;
            for (long t = num; t > 0; t >>= 1) m++;
            for (int i = 0; i < 65; i++)
                for (int j = 0; j < 65; j++) f[i, j] = -1;
            if (Dfs(m, 0, true) <= k) l = mid;
            else r = mid - 1;
        }
        return l;
    }
}
