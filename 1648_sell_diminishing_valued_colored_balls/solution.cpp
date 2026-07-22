// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& inventory, int orders) {
        const long long MOD = 1000000007;
        std::sort(inventory.rbegin(), inventory.rend());
        inventory.push_back(0);
        long long ans = 0;
        for (int i = 0; i + 1 < static_cast<int>(inventory.size()); ++i) {
            const long long width = i + 1;
            const long long high = inventory[i];
            const long long low = inventory[i + 1];
            const long long balls = width * (high - low);
            const long long take = std::min<long long>(orders, balls);
            const long long full = take / width;
            const long long rem = take % width;
            const long long bottom = high - full;
            ans += width * (high + bottom + 1) * full / 2 + rem * bottom;
            orders -= static_cast<int>(take);
            if (orders == 0) {
                break;
            }
        }
        return static_cast<int>(ans % MOD);
    }
};
