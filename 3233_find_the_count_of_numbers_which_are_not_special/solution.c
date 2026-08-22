// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

#include <math.h>
#include <stdbool.h>

enum { M3233 = 31623 };

static bool primes3233[M3233 + 1];
static int primed3233 = 0;

static void initPrimes3233(void) {
    if (primed3233) return;
    primed3233 = 1;
    for (int i = 0; i <= M3233; i++) primes3233[i] = true;
    primes3233[0] = primes3233[1] = false;
    for (int i = 2; i <= M3233; i++) {
        if (primes3233[i]) {
            for (int j = i * 2; j <= M3233; j += i) primes3233[j] = false;
        }
    }
}

int nonSpecialCount(int l, int r) {
    initPrimes3233();
    int lo = (int)ceil(sqrt((double)l));
    int hi = (int)floor(sqrt((double)r));
    int cnt = 0;
    for (int i = lo; i <= hi; i++) {
        if (primes3233[i]) cnt++;
    }
    return r - l + 1 - cnt;
}
