// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

using System.Collections.Generic;

public class Solution {
    public int Count(string num1, string num2, int min_sum, int max_sum) {
        const int MOD = 1000000007;
        string Dec(string s) {
            char[] arr = s.ToCharArray();
            int i = arr.Length - 1;
            while (i >= 0 && arr[i] == '0') { arr[i] = '9'; i--; }
            if (i >= 0) arr[i]--;
            int j = 0;
            while (j < arr.Length - 1 && arr[j] == '0') j++;
            return new string(arr, j, arr.Length - j);
        }
        int Dp(string s) {
            int n = s.Length;
            var memo = new Dictionary<(int, int, int), int>();
            int Dfs(int pos, int sum, bool tight) {
                if (sum > max_sum) return 0;
                if (pos == n) return sum >= min_sum ? 1 : 0;
                var key = (pos, sum, tight ? 1 : 0);
                if (memo.TryGetValue(key, out int cached)) return cached;
                int up = tight ? s[pos] - '0' : 9;
                int res = 0;
                for (int d = 0; d <= up; d++)
                    res = (res + Dfs(pos + 1, sum + d, tight && d == up)) % MOD;
                return memo[key] = res;
            }
            return Dfs(0, 0, true);
        }
        return (Dp(num2) - Dp(Dec(num1)) + MOD) % MOD;
    }
}
