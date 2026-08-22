// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

#include <stdlib.h>

typedef struct { long long v; int i; } P3266;

static int less3266(P3266 a, P3266 b) {
    if (a.v == b.v) return a.i < b.i;
    return a.v < b.v;
}
static void swap3266(P3266* a, P3266* b) { P3266 t=*a;*a=*b;*b=t; }
static void up3266(P3266* h, int i) {
    while (i>0){ int p=(i-1)/2; if(!less3266(h[i],h[p])) break; swap3266(&h[i],&h[p]); i=p; }
}
static void down3266(P3266* h, int n, int i) {
    for(;;){ int l=2*i+1,r=l+1,b=i;
        if(l<n&&less3266(h[l],h[b])) b=l;
        if(r<n&&less3266(h[r],h[b])) b=r;
        if(b==i) break; swap3266(&h[i],&h[b]); i=b; }
}
static long long modPow3266(long long a, long long e, long long mod) {
    long long r=1; a%=mod;
    while(e>0){ if(e&1) r=r*a%mod; a=a*a%mod; e>>=1; }
    return r;
}

int* getFinalState(int* nums, int numsSize, long long k, int multiplier, int* returnSize) {
    const int mod = 1000000007;
    *returnSize = numsSize;
    if (multiplier == 1) return nums;
    P3266* h = (P3266*)malloc((size_t)numsSize * sizeof(P3266));
    int hn = 0;
    long long maxV = 0;
    for (int i = 0; i < numsSize; i++) {
        h[hn] = (P3266){nums[i], i}; up3266(h, hn++);
        if (nums[i] > maxV) maxV = nums[i];
    }
    while (k > 0 && hn > 0) {
        P3266 p = h[0];
        h[0] = h[--hn]; if (hn) down3266(h, hn, 0);
        if (p.v * multiplier > maxV && k >= numsSize) {
            h[hn] = p; up3266(h, hn++); break;
        }
        long long nv = p.v * multiplier;
        nums[p.i] = (int)nv;
        if (nv > maxV) maxV = nv;
        h[hn] = (P3266){nv, p.i}; up3266(h, hn++);
        k--;
    }
    if (k > 0) {
        int n = numsSize;
        long long full = k / n;
        int rem = (int)(k % n);
        long long powFull = modPow3266(multiplier, full, mod);
        for (int i = 0; i < n; i++) nums[i] = (int)(nums[i] * powFull % mod);
        hn = 0;
        for (int i = 0; i < n; i++) { h[hn] = (P3266){nums[i], i}; up3266(h, hn++); }
        for (int t = 0; t < rem; t++) {
            P3266 p = h[0];
            h[0] = h[--hn]; if (hn) down3266(h, hn, 0);
            p.v = p.v * multiplier % mod;
            nums[p.i] = (int)p.v;
            h[hn] = p; up3266(h, hn++);
        }
        for (int i = 0; i < n; i++) nums[i] %= mod;
    } else {
        for (int i = 0; i < numsSize; i++) nums[i] %= mod;
    }
    free(h);
    return nums;
}
