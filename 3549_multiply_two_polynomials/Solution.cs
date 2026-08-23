// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

using System;
using System.Numerics;

public class Solution {
    void Fft(Complex[] a, bool invert) {
        int n = a.Length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) { var tmp = a[i]; a[i] = a[j]; a[j] = tmp; }
        }
        for (int length = 2; length <= n; length <<= 1) {
            double angle = 2 * Math.PI / length * (invert ? -1 : 1);
            var wlen = new Complex(Math.Cos(angle), Math.Sin(angle));
            for (int i = 0; i < n; i += length) {
                Complex w = 1;
                int half = length >> 1;
                for (int j = 0; j < half; j++) {
                    Complex u = a[i + j];
                    Complex v = a[i + j + half] * w;
                    a[i + j] = u + v;
                    a[i + j + half] = u - v;
                    w *= wlen;
                }
            }
        }
        if (invert) for (int i = 0; i < n; i++) a[i] /= n;
    }
    public long[] Multiply(int[] poly1, int[] poly2) {
        if (poly1.Length == 0 || poly2.Length == 0) return new long[0];
        int m = poly1.Length + poly2.Length - 1;
        int n = 1;
        while (n < m) n <<= 1;
        var fa = new Complex[n];
        var fb = new Complex[n];
        for (int i = 0; i < poly1.Length; i++) fa[i] = poly1[i];
        for (int i = 0; i < poly2.Length; i++) fb[i] = poly2[i];
        Fft(fa, false);
        Fft(fb, false);
        for (int i = 0; i < n; i++) fa[i] *= fb[i];
        Fft(fa, true);
        long[] res = new long[m];
        for (int i = 0; i < m; i++) res[i] = (long)Math.Round(fa[i].Real);
        return res;
    }
}
