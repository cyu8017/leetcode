// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

class Solution {
    public int superpalindromesInRange(String left, String right) {
        long L = Long.parseLong(left), R = Long.parseLong(right);
        int ans = 0;
        for (long k = 1; k <= 100000; k++) {
            String s = Long.toString(k);
            String rev = new StringBuilder(s).reverse().toString();
            long pal = Long.parseLong(s + rev);
            long sq = pal * pal;
            if (sq > R) break;
            if (sq >= L && isPal(sq)) ans++;
        }
        for (long k = 1; k <= 100000; k++) {
            String s = Long.toString(k);
            String rev = new StringBuilder(s.substring(0, s.length() - 1)).reverse().toString();
            long pal = Long.parseLong(s + rev);
            long sq = pal * pal;
            if (sq > R) break;
            if (sq >= L && isPal(sq)) ans++;
        }
        return ans;
    }

    private boolean isPal(long x) {
        String s = Long.toString(x);
        int n = s.length();
        for (int i = 0; i < n / 2; i++) if (s.charAt(i) != s.charAt(n - 1 - i)) return false;
        return true;
    }
}
