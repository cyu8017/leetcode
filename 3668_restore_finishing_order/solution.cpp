// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> recoverOrder(std::vector<int>& order, std::vector<int>& friends) {
        int n = (int)order.size();
        std::vector<int> d(n + 1);
        for (int i = 0; i < n; i++) d[order[i]] = i;
        std::sort(friends.begin(), friends.end(), [&](int a, int b) {
            return d[a] < d[b];
        });
        return friends;
    }
};
