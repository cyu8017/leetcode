// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

static long long ipow10(int n) {
    long long r = 1;
    while (n--) r *= 10;
    return r;
}

static void parse(const char* x, long long* num, long long* den) {
    char buf[64];
    strcpy(buf, x);
    char* paren = strchr(buf, '(');
    if (!paren) {
        // Fraction from decimal string via atof-ish: use double then... better manual
        double v = atof(buf);
        // convert via high precision: remove dot
        char* dot = strchr(buf, '.');
        if (!dot) { *num = atoll(buf); *den = 1; return; }
        int fracLen = (int)strlen(dot + 1);
        memmove(dot, dot + 1, strlen(dot));
        *num = atoll(buf);
        *den = ipow10(fracLen);
        return;
    }
    *paren = 0;
    char* rep = paren + 1;
    rep[strlen(rep) - 1] = 0;
    char* non = buf;
    if (!strchr(non, '.')) strcat(non, ".");
    char* dot = strchr(non, '.');
    char integer[32] = {0}, frac[32] = {0};
    strncpy(integer, non, (size_t)(dot - non));
    strcpy(frac, dot + 1);
    long long baseNum = atoll(integer);
    long long baseDen = 1;
    if (frac[0]) {
        long long f = atoll(frac);
        long long fd = ipow10((int)strlen(frac));
        baseNum = baseNum * fd + f;
        baseDen = fd;
    }
    if (rep[0]) {
        long long r = atoll(rep);
        long long rd = (ipow10((int)strlen(rep)) - 1) * baseDen;
        // base + r/rd = (baseNum*rd/baseDen + r) / rd wait
        // base = baseNum/baseDen; add r / ((10^len-1)*10^fracLen)
        long long addDen = (ipow10((int)strlen(rep)) - 1) * ipow10((int)strlen(frac));
        // result = baseNum/baseDen + r/addDen
        long long n1 = baseNum * addDen + r * baseDen;
        long long d1 = baseDen * addDen;
        *num = n1; *den = d1;
    } else {
        *num = baseNum; *den = baseDen;
    }
}

static long long gcdll(long long a, long long b) {
    if (a < 0) a = -a; if (b < 0) b = -b;
    while (b) { long long t = a % b; a = b; b = t; }
    return a;
}

bool isRationalEqual(char* s, char* t) {
    long long n1, d1, n2, d2;
    parse(s, &n1, &d1);
    parse(t, &n2, &d2);
    long long g1 = gcdll(n1, d1); n1 /= g1; d1 /= g1;
    long long g2 = gcdll(n2, d2); n2 /= g2; d2 /= g2;
    return n1 == n2 && d1 == d2;
}
