// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

#include <stdbool.h>

static bool isPalBase2081(long long x, int base) {
    int digits[64], dn = 0;
    while (x > 0) { digits[dn++] = (int)(x % base); x /= base; }
    for (int l = 0, r = dn - 1; l < r; l++, r--) if (digits[l] != digits[r]) return false;
    return true;
}

long long kMirror(int k, int n) {
    long long ans = 0;
    int count = 0;
    for (int length = 1; count < n; length++) {
        int start = 1;
        for (int i = 1; i < (length + 1) / 2; i++) start *= 10;
        int end = start * 10;
        for (int half = start; half < end && count < n; half++) {
            long long pal = half;
            if (length % 2 == 0) {
                int x = half;
                while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
            } else {
                int x = half / 10;
                while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
            }
            if (isPalBase2081(pal, k)) { ans += pal; count++; }
        }
    }
    return ans;
}
