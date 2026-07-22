// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

#include <deque>
#include <utility>
#include <vector>

class Solution {
public:
    int maxResult(std::vector<int>& nums, int k) {
        std::deque<std::pair<int, int>> q;
        q.emplace_back(0, nums[0]);
        for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
            while (q.front().first < i - k) {
                q.pop_front();
            }
            int score = nums[i] + q.front().second;
            while (!q.empty() && q.back().second <= score) {
                q.pop_back();
            }
            q.emplace_back(i, score);
        }
        return q.back().second;
    }
};
