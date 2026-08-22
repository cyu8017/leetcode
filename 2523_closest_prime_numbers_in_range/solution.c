// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int* closestPrimes(int left, int right, int* returnSize) {
    bool* isPrime = (bool*)calloc((size_t)(right + 1), sizeof(bool));
    for (int i = 2; i <= right; i++) isPrime[i] = true;
    for (int i = 2; i * i <= right; i++) {
        if (isPrime[i]) for (int j = i * i; j <= right; j += i) isPrime[j] = false;
    }
    int* primes = (int*)malloc((size_t)(right - left + 2) * sizeof(int));
    int pc = 0;
    for (int i = left; i <= right; i++) if (isPrime[i]) primes[pc++] = i;
    int* best = (int*)malloc(2 * sizeof(int));
    if (pc < 2) {
        best[0] = best[1] = -1;
    } else {
        best[0] = primes[0];
        best[1] = primes[1];
        int diff = primes[1] - primes[0];
        for (int i = 1; i + 1 < pc; i++) {
            int d = primes[i + 1] - primes[i];
            if (d < diff) { diff = d; best[0] = primes[i]; best[1] = primes[i + 1]; }
        }
    }
    free(isPrime); free(primes);
    *returnSize = 2;
    return best;
}
