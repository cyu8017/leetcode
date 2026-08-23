// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

public class Solution {
    int ModPowP(int a, int e, int p) {
        int r = 1;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % p;
            a = a * a % p;
            e >>= 1;
        }
        return r;
    }
    int ModInvPrime(int a, int p) { return ModPowP(a, p - 2, p); }
    int BinomMod(int n, int k, int p) {
        if (k < 0 || k > n) return 0;
        int num = 1, den = 1;
        for (int i = 0; i < k; i++) {
            num = num * (n - i) % p;
            den = den * (i + 1) % p;
        }
        return num * ModInvPrime(den, p) % p;
    }
    int Crt(int a1, int m1, int a2, int m2) {
        for (int x = 0; x < m1 * m2; x++) {
            if (x % m1 == a1 && x % m2 == a2) return x;
        }
        return 0;
    }
    int BinomMod10(int n, int k) {
        return Crt(BinomMod(n, k, 2), 2, BinomMod(n, k, 5), 5);
    }
    int CombineDigit(string s, int n, int offset) {
        int sum = 0;
        for (int i = 0; i <= n - 2; i++) {
            sum = (sum + BinomMod10(n - 2, i) * (s[i + offset] - '0')) % 10;
        }
        return sum;
    }
    public bool HasSameDigits(string s) {
        int n = s.Length;
        return CombineDigit(s, n, 0) == CombineDigit(s, n, 1);
    }
}
