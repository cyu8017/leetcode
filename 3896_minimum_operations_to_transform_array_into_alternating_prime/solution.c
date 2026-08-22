// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

enum { MX3896 = 200000 };
static bool isPrime3896[MX3896 + 1];
static int* primes3896;
static int primesN3896;
static int ready3896 = 0;

static void init3896(void) {
    if (ready3896) return;
    memset(isPrime3896, 1, sizeof(isPrime3896));
    isPrime3896[0] = isPrime3896[1] = false;
    for (int i = 2; i * i <= MX3896; i++) {
        if (isPrime3896[i]) {
            for (int j = i * i; j <= MX3896; j += i) isPrime3896[j] = false;
        }
    }
    primes3896 = malloc((size_t)(MX3896 / 5) * sizeof(int));
    primesN3896 = 0;
    for (int i = 2; i <= MX3896; i++) if (isPrime3896[i]) primes3896[primesN3896++] = i;
    ready3896 = 1;
}

static int lowerBoundPrime3896(int x) {
    int lo = 0, hi = primesN3896;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (primes3896[mid] >= x) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

int minOperations(int* nums, int numsSize) {
    init3896();
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (i % 2 == 0) {
            int j = lowerBoundPrime3896(x);
            ans += primes3896[j] - x;
        } else if (isPrime3896[x]) {
            ans += (x == 2) ? 2 : 1;
        }
    }
    return ans;
}
