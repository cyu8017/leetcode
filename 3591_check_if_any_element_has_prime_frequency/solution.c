// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

#include <stdbool.h>
#include <stdlib.h>

static bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++) if (x % i == 0) return false;
    return true;
}

bool checkPrimeFrequency(int* nums, int numsSize) {
    /* simple count via sort-unique */
    int* a = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) a[i] = nums[i];
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++)
            if (a[j] < a[i]) { int t = a[i]; a[i] = a[j]; a[j] = t; }
    for (int i = 0; i < numsSize; ) {
        int j = i;
        while (j < numsSize && a[j] == a[i]) j++;
        if (isPrime(j - i)) { free(a); return true; }
        i = j;
    }
    free(a);
    return false;
}
