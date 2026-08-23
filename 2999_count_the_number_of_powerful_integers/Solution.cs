// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

using System.Collections.Generic;

public class Solution {
    public long NumberOfPowerfulInt(long start, long finish, int limit, string s) {
        long Count(long num) {
            if (num < 0) return 0;
            foreach (char c in s) if (c - '0' > limit) return 0;
            string t = num.ToString();
            int n = t.Length, sn = s.Length;
            if (n < sn) return 0;
            long ans = 0;
            for (int length = sn; length < n; length++) {
                int preLen = length - sn;
                if (preLen == 0) {
                    ans += 1;
                } else {
                    long ways = limit;
                    for (int i = 1; i < preLen; i++) ways *= (limit + 1);
                    ans += ways;
                }
            }
            int pref = n - sn;
            var memo = new Dictionary<(int, int), long>();
            long Dfs(int i, bool tight) {
                if (i == pref) {
                    if (tight) return string.CompareOrdinal(t.Substring(pref), s) >= 0 ? 1 : 0;
                    return 1;
                }
                var key = (i, tight ? 1 : 0);
                if (memo.TryGetValue(key, out long cached)) return cached;
                int up = tight ? t[i] - '0' : limit;
                if (up > limit) up = limit;
                long res = 0;
                for (int d = 0; d <= up; d++) {
                    if (i == 0 && d == 0) continue;
                    res += Dfs(i + 1, tight && d == (t[i] - '0'));
                }
                return memo[key] = res;
            }
            ans += Dfs(0, true);
            return ans;
        }
        return Count(finish) - Count(start - 1);
    }
}
