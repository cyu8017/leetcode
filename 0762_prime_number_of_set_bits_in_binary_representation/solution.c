// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

#include <stdbool.h>

static bool isPrimeBits(int n) {
    static const int primes[] = {2, 3, 5, 7, 11, 13, 17, 19};
    for (int i = 0; i < 8; i++) if (primes[i] == n) return true;
    return false;
}

int countPrimeSetBits(int left, int right) {
    int ans = 0;
    for (int num = left; num <= right; num++) {
        int bits = 0;
        for (unsigned x = (unsigned)num; x; x >>= 1) bits += (int)(x & 1u);
        if (isPrimeBits(bits)) ans++;
    }
    return ans;
}
