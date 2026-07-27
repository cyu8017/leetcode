// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

#include <vector>

class Solution {
public:
    bool carPooling(std::vector<std::vector<int>>& trips, int capacity) {
        std::vector<int> diff(1001, 0);
        for (const auto& trip : trips) {
            diff[trip[1]] += trip[0];
            diff[trip[2]] -= trip[0];
        }
        int cur = 0;
        for (int x : diff) {
            cur += x;
            if (cur > capacity) {
                return false;
            }
        }
        return true;
    }
};
