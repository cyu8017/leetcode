// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

public class Solution {
    public int NumberOfBeautifulIntegers(int low, int high, int k) {
        int Count(int n) {
            if (n < 0) return 0;
            string s = n.ToString();
            int[,,,,] memo = new int[12, 45, 22, 2, 2];
            for (int a = 0; a < 12; a++)
                for (int b = 0; b < 45; b++)
                    for (int c = 0; c < 22; c++)
                        for (int d = 0; d < 2; d++)
                            for (int e = 0; e < 2; e++) memo[a, b, c, d, e] = -1;
            int Dfs(int pos, int diff, int mod, int tight, int started) {
                if (pos == s.Length) return (started == 1 && diff == 0 && mod == 0) ? 1 : 0;
                ref int res = ref memo[pos, diff + 20, mod, tight, started];
                if (res != -1) return res;
                int up = tight == 1 ? s[pos] - '0' : 9;
                int ans = 0;
                for (int digit = 0; digit <= up; digit++) {
                    int nt = (tight == 1 && digit == up) ? 1 : 0;
                    if (started == 0) {
                        if (digit == 0) ans += Dfs(pos + 1, diff, mod, nt, 0);
                        else {
                            int nd = diff + (digit % 2 == 0 ? 1 : -1);
                            ans += Dfs(pos + 1, nd, digit % k, nt, 1);
                        }
                    } else {
                        int nd = diff + (digit % 2 == 0 ? 1 : -1);
                        ans += Dfs(pos + 1, nd, (mod * 10 + digit) % k, nt, 1);
                    }
                }
                return res = ans;
            }
            return Dfs(0, 0, 0, 1, 0);
        }
        return Count(high) - Count(low - 1);
    }
}
