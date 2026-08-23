// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

class Solution {
    private int modPowP(int a, int e, int p) {
        int r = 1;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % p;
            a = a * a % p;
            e >>= 1;
        }
        return r;
    }
    private int modInvPrime(int a, int p) { return modPowP(a, p - 2, p); }
    private int binomMod(int n, int k, int p) {
        if (k < 0 || k > n) return 0;
        int num = 1, den = 1;
        for (int i = 0; i < k; i++) {
            num = num * (n - i) % p;
            den = den * (i + 1) % p;
        }
        return num * modInvPrime(den, p) % p;
    }
    private int crt(int a1, int m1, int a2, int m2) {
        for (int x = 0; x < m1 * m2; x++) {
            if (x % m1 == a1 && x % m2 == a2) return x;
        }
        return 0;
    }
    private int binomMod10(int n, int k) {
        return crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5);
    }
    private int combineDigit(String s, int n, int offset) {
        int sum = 0;
        for (int i = 0; i <= n - 2; i++) {
            sum = (sum + binomMod10(n - 2, i) * (s.charAt(i + offset) - '0')) % 10;
        }
        return sum;
    }
    public boolean hasSameDigits(String s) {
        int n = s.length();
        return combineDigit(s, n, 0) == combineDigit(s, n, 1);
    }
}
