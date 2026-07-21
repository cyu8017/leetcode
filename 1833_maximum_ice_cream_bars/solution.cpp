// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxIceCream(std::vector<int>& costs, int coins) {
        std::sort(costs.begin(), costs.end());
        int count = 0;
        for (int cost : costs) {
            if (coins < cost) {
                break;
            }
            coins -= cost;
            ++count;
        }
        return count;
    }
};
