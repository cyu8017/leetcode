// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

#include <algorithm>
#include <vector>

class Solution {
public:
    double maxPrice(std::vector<std::vector<int>>& items, int capacity) {
        std::sort(items.begin(), items.end(), [](const auto& a, const auto& b) {
            return (double)a[0] / a[1] > (double)b[0] / b[1];
        });
        double ans = 0.0;
        int remain = capacity;
        for (const auto& it : items) {
            int price = it[0], weight = it[1];
            if (remain >= weight) {
                ans += price;
                remain -= weight;
            } else {
                ans += (double)price * remain / weight;
                remain = 0;
                break;
            }
        }
        if (remain > 0) return -1;
        return ans;
    }
};
