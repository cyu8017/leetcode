// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool primeSubOperation(int* nums, int numsSize) {
    int maxV = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxV) maxV = nums[i];
    bool* isP = (bool*)calloc((size_t)(maxV + 1), sizeof(bool));
    for (int i = 2; i <= maxV; i++) isP[i] = true;
    for (int i = 2; i * i <= maxV; i++) {
        if (isP[i]) for (int j = i * i; j <= maxV; j += i) isP[j] = false;
    }
    int* primes = (int*)malloc((size_t)(maxV + 1) * sizeof(int));
    int pc = 0;
    for (int i = 2; i <= maxV; i++) if (isP[i]) primes[pc++] = i;
    int prev = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x <= prev) { free(isP); free(primes); return false; }
        int best = x;
        for (int j = 0; j < pc; j++) {
            int p = primes[j];
            if (p >= x) break;
            if (x - p > prev) best = x - p;
        }
        prev = best;
    }
    free(isP); free(primes);
    return true;
}
