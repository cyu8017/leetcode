// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

#include <string.h>

int countOddLetters(int n) {
    static const char* d[] = {
        "zero","one","two","three","four","five","six","seven","eight","nine"
    };
    int mask = 0;
    if (n == 0) {
        const char* s = d[0];
        for (int i = 0; s[i]; i++) mask ^= 1 << (s[i] - 'a');
    }
    while (n > 0) {
        int x = n % 10;
        n /= 10;
        const char* s = d[x];
        for (int i = 0; s[i]; i++) mask ^= 1 << (s[i] - 'a');
    }
    int cnt = 0;
    while (mask) { cnt += mask & 1; mask >>= 1; }
    return cnt;
}
