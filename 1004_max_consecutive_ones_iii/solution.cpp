// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestOnes(std::vector<int>& nums, int k) {
        int left = 0, zeros = 0, ans = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            zeros += nums[right] == 0;
            while (zeros > k) {
                zeros -= nums[left] == 0;
                ++left;
            }
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};

