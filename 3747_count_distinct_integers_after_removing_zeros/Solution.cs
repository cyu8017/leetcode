// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

public class Solution {
    public long CountDistinct(long n) {
        string s = n.ToString();
        int m = s.Length;
        long[,,,] f = new long[20, 2, 2, 2];
        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    for (int t = 0; t < 2; t++)
                        f[i, j, k, t] = -1;

        long Dfs(int i, int zero, int lead, int limit) {
            if (i == m) return (zero == 0 && lead == 0) ? 1 : 0;
            if (limit == 0 && f[i, zero, lead, limit] != -1) return f[i, zero, lead, limit];
            int up = limit != 0 ? s[i] - '0' : 9;
            long ans = 0;
            for (int d = 0; d <= up; d++) {
                int nxtZero = zero;
                if (d == 0 && lead == 0) nxtZero = 1;
                int nxtLead = (lead == 1 && d == 0) ? 1 : 0;
                int nxtLimit = (limit == 1 && d == up) ? 1 : 0;
                ans += Dfs(i + 1, nxtZero, nxtLead, nxtLimit);
            }
            if (limit == 0) f[i, zero, lead, limit] = ans;
            return ans;
        }
        return Dfs(0, 0, 1, 1);
    }
}
