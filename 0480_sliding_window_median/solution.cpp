// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<double> medianSlidingWindow(std::vector<int>& nums, int k) {
        std::vector<int> window(nums.begin(), nums.begin() + k);
        std::sort(window.begin(), window.end());
        std::vector<double> result;

        auto appendMedian = [&]() {
            if (k % 2) {
                result.push_back(static_cast<double>(window[k / 2]));
            } else {
                result.push_back((window[k / 2 - 1] + window[k / 2]) / 2.0);
            }
        };

        appendMedian();
        for (int index = k; index < static_cast<int>(nums.size()); ++index) {
            const int outgoing = nums[index - k];
            const int incoming = nums[index];
            const auto position = std::lower_bound(window.begin(), window.end(), outgoing);
            window.erase(position);
            const auto insertPosition = std::lower_bound(window.begin(), window.end(), incoming);
            window.insert(insertPosition, incoming);
            appendMedian();
        }
        return result;
    }
};
