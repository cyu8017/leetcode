// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

#include <stdbool.h>

bool isArmstrong(int n) {
    int digits = 0, x = n;
    while (x) { digits++; x /= 10; }
    if (n == 0) digits = 1;
    long long sum = 0;
    x = n;
    while (x) {
        int d = x % 10;
        long long p = 1;
        for (int i = 0; i < digits; i++) p *= d;
        sum += p;
        x /= 10;
    }
    return sum == n;
}
