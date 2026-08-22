// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

#include <stdbool.h>

static bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; (long long)i * i <= x; i++) if (x % i == 0) return false;
    return true;
}

int diagonalPrime(int** nums, int numsSize, int* numsColSize) {
    (void)numsColSize;
    int n = numsSize, best = 0;
    for (int i = 0; i < n; i++) {
        int a = nums[i][i], b = nums[i][n - 1 - i];
        if (isPrime(a) && a > best) best = a;
        if (isPrime(b) && b > best) best = b;
    }
    return best;
}
