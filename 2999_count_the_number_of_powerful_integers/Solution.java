// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private String s;
    private int limit;

    private long count(long num) {
        if (num < 0) return 0;
        for (int i = 0; i < s.length(); i++) if (s.charAt(i) - '0' > limit) return 0;
        String t = Long.toString(num);
        int n = t.length(), sn = s.length();
        if (n < sn) return 0;
        long ans = 0;
        for (int length = sn; length < n; length++) {
            int preLen = length - sn;
            if (preLen == 0) ans += 1;
            else {
                long ways = limit;
                for (int i = 1; i < preLen; i++) ways *= (limit + 1);
                ans += ways;
            }
        }
        int pref = n - sn;
        Map<Long, Long> memo = new HashMap<>();
        ans += dfs(t, pref, 0, true, memo);
        return ans;
    }

    private long dfs(String t, int pref, int i, boolean tight, Map<Long, Long> memo) {
        if (i == pref) {
            if (tight) return t.substring(pref).compareTo(s) >= 0 ? 1 : 0;
            return 1;
        }
        long key = (((long) i) << 1) | (tight ? 1 : 0);
        if (memo.containsKey(key)) return memo.get(key);
        int up = tight ? t.charAt(i) - '0' : limit;
        if (up > limit) up = limit;
        long res = 0;
        for (int d = 0; d <= up; d++) {
            if (i == 0 && d == 0) continue;
            res += dfs(t, pref, i + 1, tight && d == (t.charAt(i) - '0'), memo);
        }
        memo.put(key, res);
        return res;
    }

    public long numberOfPowerfulInt(long start, long finish, int limit, String s) {
        this.s = s;
        this.limit = limit;
        return count(finish) - count(start - 1);
    }
}
