// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

#include <deque>
#include <vector>

class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        std::deque<int> window;
        std::vector<int> result;

        for (int index = 0; index < static_cast<int>(nums.size()); index++) {
            while (!window.empty() && nums[window.back()] <= nums[index]) {
                window.pop_back();
            }
            window.push_back(index);
            if (window.front() <= index - k) {
                window.pop_front();
            }
            if (index >= k - 1) {
                result.push_back(nums[window.front()]);
            }
        }

        return result;
    }
};
