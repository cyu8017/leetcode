// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestNiceSubarray(std::vector<int>& nums) {
        int used = 0, left = 0, ans = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            while (used & nums[right]) {
                used ^= nums[left];
                left++;
            }
            used |= nums[right];
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};
