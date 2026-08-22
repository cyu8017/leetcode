// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

#include <stdbool.h>
bool checkDivisibility(int n) {
    int s = 0, p = 1, x = n;
    while (x) { int v = x % 10; x /= 10; s += v; p *= v; }
    return n % (s + p) == 0;
}
