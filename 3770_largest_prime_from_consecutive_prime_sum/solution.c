// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MX 500000

static bool* isPrimeArr;
static int* S;
static int SN;
static int inited = 0;

static void ensureInit(void) {
    if (inited) return;
    inited = 1;
    isPrimeArr = (bool*)malloc((size_t)(MX + 1) * sizeof(bool));
    for (int i = 0; i <= MX; i++) isPrimeArr[i] = true;
    isPrimeArr[0] = isPrimeArr[1] = false;
    int* primes = (int*)malloc((size_t)(MX / 2) * sizeof(int));
    int pn = 0;
    for (int i = 2; i <= MX; i++) {
        if (isPrimeArr[i]) {
            primes[pn++] = i;
            if ((long long)i * i <= MX) {
                for (int j = i * i; j <= MX; j += i) isPrimeArr[j] = false;
            }
        }
    }
    S = (int*)malloc((size_t)(pn + 2) * sizeof(int));
    SN = 0;
    S[SN++] = 0;
    int t = 0;
    for (int i = 0; i < pn; i++) {
        t += primes[i];
        if (t > MX) break;
        if (isPrimeArr[t]) S[SN++] = t;
    }
    free(primes);
}

static int lowerBound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}

int largestPrime(int n) {
    ensureInit();
    int i = lowerBound(S, SN, n + 1);
    return S[i - 1];
}
