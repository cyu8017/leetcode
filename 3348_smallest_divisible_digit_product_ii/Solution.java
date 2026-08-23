// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

class Solution {
    private boolean dfs(char[] res, int i, boolean tight, boolean sameLen, String num, long t) {
        if (i == res.length) {
            long prod = 1;
            for (char c : res) {
                prod *= (c - '0');
                if (prod == 0) break;
            }
            return prod % t == 0 && prod > 0;
        }
        char start = (i == 0) ? '1' : '0';
        if (tight && sameLen && i < num.length()) start = num.charAt(i);
        for (char c = start; c <= '9'; c++) {
            res[i] = c;
            boolean nt = tight && sameLen && i < num.length() && c == num.charAt(i);
            if (dfs(res, i + 1, nt, sameLen, num, t)) return true;
        }
        return false;
    }

    public String smallestNumber(String num, long t) {
        long tt = t;
        for (int d = 9; d >= 2; d--) {
            while (tt % d == 0) tt /= d;
        }
        if (tt > 1) return "-1";
        for (int extra = 0; extra <= 60; extra++) {
            int L = num.length() + extra;
            char[] res = new char[L];
            if (dfs(res, 0, true, extra == 0, num, t)) return new String(res);
        }
        return "-1";
    }
}
