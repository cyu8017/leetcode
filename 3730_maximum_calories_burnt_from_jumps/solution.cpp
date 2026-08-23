// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxCaloriesBurnt(std::vector<int>& heights) {
        std::sort(heights.begin(), heights.end());
        long long ans = 0;
        int pre = 0, l = 0, r = (int)heights.size() - 1;
        while (l < r) {
            long long d1 = heights[r] - pre;
            ans += d1 * d1;
            long long d2 = heights[l] - heights[r];
            ans += d2 * d2;
            pre = heights[l];
            l++;
            r--;
        }
        long long d = heights[r] - pre;
        ans += d * d;
        return ans;
    }
};
