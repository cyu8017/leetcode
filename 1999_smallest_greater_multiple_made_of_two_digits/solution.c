// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

#include <stdlib.h>

int findInteger(int k, int digit1, int digit2) {
    int digits[2];
    int dn = 0;
    digits[dn++] = digit1;
    if (digit2 != digit1) digits[dn++] = digit2;
    if (digits[0] > digits[1] && dn == 2) {
        int t = digits[0]; digits[0] = digits[1]; digits[1] = t;
    }
    long long* q = (long long*)malloc(200000 * sizeof(long long));
    char* seen = NULL;
    (void)seen;
    int head = 0, tail = 0;
    for (int i = 0; i < dn; i++) {
        if (digits[i] != 0) q[tail++] = digits[i];
    }
    if (!tail) { free(q); return -1; }
    while (head < tail) {
        long long x = q[head++];
        if (x > k && x % k == 0) {
            free(q);
            return (int)x;
        }
        for (int i = 0; i < dn; i++) {
            long long nx = x * 10 + digits[i];
            if (nx <= 2147483647LL && tail < 200000) {
                q[tail++] = nx;
            }
        }
    }
    free(q);
    return -1;
}
