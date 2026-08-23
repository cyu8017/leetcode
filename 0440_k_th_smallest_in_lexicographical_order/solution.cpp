// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

#include <algorithm>

class Solution {
    long long countSteps(int n, long long first, long long last) {
        long long steps = 0;
        while (first <= n) {
            steps += std::min(static_cast<long long>(n) + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }

public:
    int findKthNumber(int n, int k) {
        long long current = 1;
        long long remaining = k - 1;

        while (remaining > 0) {
            long long steps = countSteps(n, current, current + 1);
            if (steps <= remaining) {
                ++current;
                remaining -= steps;
            } else {
                current *= 10;
                --remaining;
            }
        }

        return static_cast<int>(current);
    }
};
