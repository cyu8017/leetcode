// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int convertArray(std::vector<int>& nums) {
        auto cost = [](const std::vector<int>& arr) {
            std::priority_queue<int> h;
            int ans = 0;
            for (int x : arr) {
                if (!h.empty() && h.top() > x) {
                    ans += h.top() - x;
                    h.pop();
                    h.push(x);
                }
                h.push(x);
            }
            return ans;
        };
        std::vector<int> rev(nums.rbegin(), nums.rend());
        return std::min(cost(nums), cost(rev));
    }
};
