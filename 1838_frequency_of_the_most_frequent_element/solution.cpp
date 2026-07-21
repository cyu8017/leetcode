// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int left = 0;
        long long windowSum = 0;
        int best = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            windowSum += nums[right];
            while (static_cast<long long>(nums[right]) * (right - left + 1) - windowSum > k) {
                windowSum -= nums[left];
                ++left;
            }
            best = std::max(best, right - left + 1);
        }
        return best;
    }
};
