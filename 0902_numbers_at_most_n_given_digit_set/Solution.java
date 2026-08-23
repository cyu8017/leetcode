// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution {
    private String[] digits;
    private int k;

    public int atMostNGivenDigitSet(String[] digits, int n) {
        this.digits = digits;
        this.k = digits.length;
        String s = Integer.toString(n);
        int m = s.length();
        int ans = 0;
        for (int i = 1; i < m; i++) ans += ipow(k, i);
        ans += countUpTo(s);
        return ans;
    }

    private int ipow(int bas, int exp) {
        int r = 1;
        while (exp-- > 0) r *= bas;
        return r;
    }

    private int countUpTo(String t) {
        if (t.length() == 0) return 0;
        int first = 0;
        for (String d : digits) if (d.charAt(0) < t.charAt(0)) first++;
        int ways = first * ipow(k, t.length() - 1);
        boolean found = false;
        for (String d : digits) {
            if (d.charAt(0) == t.charAt(0)) { found = true; break; }
        }
        if (found) ways += countUpTo(t.substring(1));
        return ways;
    }
}
