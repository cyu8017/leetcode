// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

using System.Collections.Generic;
using System.Text;

public class Solution {
    const int MOD = 1000000007;

    List<int> ToDigits(string s, int b) {
        if (s == "0") return new List<int> { 0 };
        var digs = new List<int>();
        while (!(s.Length == 1 && s[0] == '0')) {
            int rem = 0;
            var q = new StringBuilder();
            foreach (char c in s) {
                int cur = rem * 10 + (c - '0');
                int d = cur / b;
                rem = cur % b;
                if (q.Length > 0 || d != 0) q.Append((char)('0' + d));
            }
            digs.Add(rem);
            s = q.Length == 0 ? "0" : q.ToString();
        }
        digs.Reverse();
        return digs;
    }

    string Dec(string s) {
        char[] arr = s.ToCharArray();
        int i = arr.Length - 1;
        while (i >= 0 && arr[i] == '0') { arr[i] = '9'; i--; }
        if (i < 0) return "0";
        arr[i]--;
        int p = 0;
        while (p + 1 < arr.Length && arr[p] == '0') p++;
        return new string(arr, p, arr.Length - p);
    }

    int CountUpto(List<int> digs, int b) {
        int m = digs.Count;
        var memo = new Dictionary<(int, int, int), int>();
        int Dfs(int pos, int last, bool tight) {
            if (pos == m) return 1;
            var key = (pos, last, tight ? 1 : 0);
            if (memo.ContainsKey(key)) return memo[key];
            int up = tight ? digs[pos] : b - 1;
            int res = 0;
            for (int d = last; d <= up; d++)
                res = (res + Dfs(pos + 1, d, tight && d == up)) % MOD;
            return memo[key] = res;
        }
        return Dfs(0, 0, true);
    }

    public int CountNumbers(string l, string r, int b) {
        var rd = ToDigits(r, b);
        var ld = ToDigits(Dec(l), b);
        return (CountUpto(rd, b) - CountUpto(ld, b) + MOD) % MOD;
    }
}
