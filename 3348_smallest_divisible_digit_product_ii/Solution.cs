// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

public class Solution {
    bool Dfs(char[] res, int i, bool tight, bool sameLen, string num, long t) {
        if (i == res.Length) {
            long prod = 1;
            foreach (char c in res) {
                prod *= (c - '0');
                if (prod == 0) break;
            }
            return prod % t == 0 && prod > 0;
        }
        char start = (i == 0) ? '1' : '0';
        if (tight && sameLen && i < num.Length) start = num[i];
        for (char c = start; c <= '9'; c++) {
            res[i] = c;
            bool nt = tight && sameLen && i < num.Length && c == num[i];
            if (Dfs(res, i + 1, nt, sameLen, num, t)) return true;
        }
        return false;
    }

    public string SmallestNumber(string num, long t) {
        long tt = t;
        for (int d = 9; d >= 2; d--) {
            while (tt % d == 0) tt /= d;
        }
        if (tt > 1) return "-1";
        for (int extra = 0; extra <= 60; extra++) {
            int L = num.Length + extra;
            char[] res = new char[L];
            if (Dfs(res, 0, true, extra == 0, num, t)) return new string(res);
        }
        return "-1";
    }
}
