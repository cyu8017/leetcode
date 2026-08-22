// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

#include <stdbool.h>
#include <stdio.h>
#include <string.h>

static bool isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++) if (x % i == 0) return false;
    return true;
}

bool completePrime(int num) {
    char s[32];
    sprintf(s, "%d", num);
    int n = (int)strlen(s);
    int x = 0;
    for (int i = 0; i < n; i++) {
        x = x * 10 + (s[i] - '0');
        if (!isPrime(x)) return false;
    }
    x = 0; int p = 1;
    for (int i = n - 1; i >= 0; i--) {
        x = p * (s[i] - '0') + x;
        p *= 10;
        if (!isPrime(x)) return false;
    }
    return true;
}
