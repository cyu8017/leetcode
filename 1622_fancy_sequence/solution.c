// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

#include <stdlib.h>

#define MOD 1000000007LL

typedef struct {
    long long* vals;
    int n;
    int cap;
    long long mul;
    long long add;
} Fancy;

static long long modPow(long long base, long long exp) {
    long long r = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) r = r * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    return r;
}

Fancy* fancyCreate(void) {
    Fancy* obj = (Fancy*)calloc(1, sizeof(Fancy));
    obj->mul = 1;
    return obj;
}

void fancyAppend(Fancy* obj, int val) {
    if (obj->n == obj->cap) {
        obj->cap = obj->cap ? obj->cap * 2 : 16;
        obj->vals = (long long*)realloc(obj->vals, (size_t)obj->cap * sizeof(long long));
    }
    long long inv = modPow(obj->mul, MOD - 2);
    obj->vals[obj->n++] = ((val - obj->add) % MOD + MOD) % MOD * inv % MOD;
}

void fancyAddAll(Fancy* obj, int inc) {
    if (obj->n) obj->add = (obj->add + inc) % MOD;
}

void fancyMultAll(Fancy* obj, int m) {
    if (!obj->n) return;
    obj->mul = obj->mul * m % MOD;
    obj->add = obj->add * m % MOD;
}

int fancyGetIndex(Fancy* obj, int idx) {
    if (idx >= obj->n) return -1;
    return (int)((obj->vals[idx] * obj->mul + obj->add) % MOD);
}

void fancyFree(Fancy* obj) {
    if (!obj) return;
    free(obj->vals);
    free(obj);
}
