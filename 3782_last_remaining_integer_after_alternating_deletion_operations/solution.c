// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

#include <stdbool.h>

long long lastRemaining(long long n) {
    long long first = 1, step = 2;
    bool left = true;
    while (n > 1) {
        if (!left && n % 2 == 0) first += step;
        n = (n + 1) / 2;
        step *= 2;
        left = !left;
    }
    return first;
}
