// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

#include <math.h>
#include <stdlib.h>

typedef struct { double re, im; } C3549;

static C3549 cmul(C3549 a, C3549 b) {
    return (C3549){a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re};
}
static C3549 cadd(C3549 a, C3549 b) { return (C3549){a.re + b.re, a.im + b.im}; }
static C3549 csub(C3549 a, C3549 b) { return (C3549){a.re - b.re, a.im - b.im}; }

static void fft(C3549* a, int n, int invert) {
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) { C3549 t = a[i]; a[i] = a[j]; a[j] = t; }
    }
    for (int length = 2; length <= n; length <<= 1) {
        double angle = 2 * 3.14159265358979323846 / length * (invert ? -1 : 1);
        C3549 wlen = {cos(angle), sin(angle)};
        for (int i = 0; i < n; i += length) {
            C3549 w = {1, 0};
            int half = length >> 1;
            for (int j = 0; j < half; j++) {
                C3549 u = a[i + j];
                C3549 v = cmul(a[i + j + half], w);
                a[i + j] = cadd(u, v);
                a[i + j + half] = csub(u, v);
                w = cmul(w, wlen);
            }
        }
    }
    if (invert) for (int i = 0; i < n; i++) { a[i].re /= n; a[i].im /= n; }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* multiply(int* poly1, int poly1Size, int* poly2, int poly2Size, int* returnSize) {
    if (poly1Size == 0 || poly2Size == 0) { *returnSize = 0; return NULL; }
    int m = poly1Size + poly2Size - 1;
    int n = 1;
    while (n < m) n <<= 1;
    C3549* fa = (C3549*)calloc((size_t)n, sizeof(C3549));
    C3549* fb = (C3549*)calloc((size_t)n, sizeof(C3549));
    for (int i = 0; i < poly1Size; i++) fa[i].re = poly1[i];
    for (int i = 0; i < poly2Size; i++) fb[i].re = poly2[i];
    fft(fa, n, 0); fft(fb, n, 0);
    for (int i = 0; i < n; i++) fa[i] = cmul(fa[i], fb[i]);
    fft(fa, n, 1);
    long long* res = (long long*)malloc((size_t)m * sizeof(long long));
    for (int i = 0; i < m; i++) res[i] = (long long)llround(fa[i].re);
    free(fa); free(fb);
    *returnSize = m;
    return res;
}
