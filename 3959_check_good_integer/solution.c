// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/

#include <stdbool.h>

bool checkGoodInteger(int n) {
    int s = 0;
    for (; n > 0; n /= 10) {
        int x = n % 10;
        s += x * (x - 1);
    }
    return s >= 50;
}
