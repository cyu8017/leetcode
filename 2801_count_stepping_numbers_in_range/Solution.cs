// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

using System;

public class Solution {
    public int CountSteppingNumbers(string low, string high) {
        const int MOD = 1000000007;
        int CountTo(string s) {
            int[,,,] memo = new int[85, 2, 11, 2];
            for (int i = 0; i < 85; i++)
                for (int j = 0; j < 2; j++)
                    for (int k = 0; k < 11; k++)
                        for (int l = 0; l < 2; l++) memo[i, j, k, l] = -1;
            int Dfs(int pos, int tight, int last, int started) {
                if (pos == s.Length) return started;
                ref int res = ref memo[pos, tight, last + 1, started];
                if (res != -1) return res;
                int up = tight == 1 ? s[pos] - '0' : 9;
                long ans = 0;
                for (int d = 0; d <= up; d++) {
                    int nt = (tight == 1 && d == up) ? 1 : 0;
                    if (started == 0) {
                        if (d == 0) ans += Dfs(pos + 1, nt, -1, 0);
                        else ans += Dfs(pos + 1, nt, d, 1);
                    } else if (Math.Abs(d - last) == 1) {
                        ans += Dfs(pos + 1, nt, d, 1);
                    }
                }
                return res = (int)(ans % MOD);
            }
            return Dfs(0, 1, -1, 0);
        }
        string Dec(string s) {
            char[] arr = s.ToCharArray();
            int i = arr.Length - 1;
            while (i >= 0 && arr[i] == '0') { arr[i] = '9'; i--; }
            if (i >= 0) arr[i]--;
            int j = 0;
            while (j < arr.Length - 1 && arr[j] == '0') j++;
            return new string(arr, j, arr.Length - j);
        }
        int ans2 = (CountTo(high) - CountTo(Dec(low))) % MOD;
        if (ans2 < 0) ans2 += MOD;
        return ans2;
    }
}
