// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

#include <algorithm>
#include <vector>

class Solution {
public:
    int getMaximumConsecutive(std::vector<int>& coins) {
        std::sort(coins.begin(), coins.end());
        long long reach = 0;
        for (int coin : coins) {
            if (coin > reach + 1) break;
            reach += coin;
        }
        return (int)(reach + 1);
    }
};
