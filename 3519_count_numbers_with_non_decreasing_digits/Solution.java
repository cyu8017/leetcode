// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    static final int MOD = 1_000_000_007;

    List<Integer> toDigits(String s, int b) {
        if (s.equals("0")) {
            List<Integer> z = new ArrayList<>();
            z.add(0);
            return z;
        }
        List<Integer> digs = new ArrayList<>();
        while (!(s.length() == 1 && s.charAt(0) == '0')) {
            int rem = 0;
            StringBuilder q = new StringBuilder();
            for (char c : s.toCharArray()) {
                int cur = rem * 10 + (c - '0');
                int d = cur / b;
                rem = cur % b;
                if (q.length() > 0 || d != 0) q.append((char) ('0' + d));
            }
            digs.add(rem);
            s = q.length() == 0 ? "0" : q.toString();
        }
        Collections.reverse(digs);
        return digs;
    }

    String dec(String s) {
        char[] a = s.toCharArray();
        int i = a.length - 1;
        while (i >= 0 && a[i] == '0') { a[i] = '9'; i--; }
        if (i < 0) return "0";
        a[i]--;
        String t = new String(a);
        int p = 0;
        while (p + 1 < t.length() && t.charAt(p) == '0') p++;
        return t.substring(p);
    }

    int countUpto(List<Integer> digs, int b) {
        int m = digs.size();
        Map<String, Integer> memo = new HashMap<>();
        return dfs(0, 0, true, digs, b, m, memo);
    }

    int dfs(int pos, int last, boolean tight, List<Integer> digs, int b, int m, Map<String, Integer> memo) {
        if (pos == m) return 1;
        String key = pos + "," + last + "," + (tight ? 1 : 0);
        if (memo.containsKey(key)) return memo.get(key);
        int up = tight ? digs.get(pos) : b - 1;
        int res = 0;
        for (int d = last; d <= up; d++)
            res = (res + dfs(pos + 1, d, tight && d == up, digs, b, m, memo)) % MOD;
        memo.put(key, res);
        return res;
    }

    public int countNumbers(String l, String r, int b) {
        List<Integer> rd = toDigits(r, b);
        List<Integer> ld = toDigits(dec(l), b);
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD;
    }
}
