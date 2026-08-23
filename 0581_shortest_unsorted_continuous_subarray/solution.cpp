// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findUnsortedSubarray(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int left = -1;
        int right = -2;
        int maxSeen = nums[0];
        int minSeen = nums[n - 1];
        for (int i = 0; i < n; ++i) {
            maxSeen = std::max(maxSeen, nums[i]);
            if (nums[i] < maxSeen) {
                right = i;
            }
            int j = n - 1 - i;
            minSeen = std::min(minSeen, nums[j]);
            if (nums[j] > minSeen) {
                left = j;
            }
        }
        return right - left + 1;
    }
};
