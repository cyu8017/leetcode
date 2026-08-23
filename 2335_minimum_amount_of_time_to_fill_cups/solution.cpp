// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

#include <algorithm>
#include <vector>

class Solution {
public:
    int fillCups(std::vector<int>& amount) {
        int a = amount[0], b = amount[1], c = amount[2];
        if (a < b) std::swap(a, b);
        if (a < c) std::swap(a, c);
        if (b < c) std::swap(b, c);
        if (a >= b + c) return a;
        return (a + b + c + 1) / 2;
    }
};
