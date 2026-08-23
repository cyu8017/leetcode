// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

#include <bit>

class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        for (int k = 1; k <= 60; k++) {
            long long rem = num1 - 1LL * k * num2;
            if (rem < k) continue;
            if (__builtin_popcountll(rem) <= k) return k;
        }
        return -1;
    }
};
