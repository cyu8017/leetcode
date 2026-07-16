// LeetCode 0204 - Count Primes
#include <stdbool.h>
#include <stdlib.h>
int countPrimes(int n) { if (n <= 2) return 0; bool* prime = malloc((size_t)n * sizeof(bool)); for (int i = 0; i < n; ++i) prime[i] = true; prime[0] = prime[1] = false; for (int p = 2; p * p < n; ++p) if (prime[p]) for (int m = p * p; m < n; m += p) prime[m] = false; int count = 0; for (int i = 0; i < n; ++i) count += prime[i]; free(prime); return count; }
