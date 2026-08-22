// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

#include <stdlib.h>

static int minInt(int left, int right) {
    return left < right ? left : right;
}

int nthSuperUglyNumber(int n, int* primes, int primesSize) {
    int* ugly = (int*)malloc((size_t)n * sizeof(int));
    int uglySize = 1;
    ugly[0] = 1;

    int* pointers = (int*)calloc((size_t)primesSize, sizeof(int));
    long long* nextValues = (long long*)malloc((size_t)primesSize * sizeof(long long));

    while (uglySize < n) {
        for (int index = 0; index < primesSize; index++) {
            nextValues[index] = (long long)ugly[pointers[index]] * primes[index];
        }
        long long nextUgly = nextValues[0];
        for (int index = 1; index < primesSize; index++) {
            if (nextValues[index] < nextUgly) {
                nextUgly = nextValues[index];
            }
        }
        ugly[uglySize++] = (int)nextUgly;
        for (int index = 0; index < primesSize; index++) {
            if (nextUgly == (long long)ugly[pointers[index]] * primes[index]) {
                pointers[index] += 1;
            }
        }
    }

    int answer = ugly[uglySize - 1];
    free(ugly);
    free(pointers);
    free(nextValues);
    return answer;
}
