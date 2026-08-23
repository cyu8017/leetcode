// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestAlternatingSubarray(std::vector<int>& nums, int threshold) {
        int ans = 0, n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 != 0 || nums[i] > threshold) continue;
            int j = i;
            while (j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2) j++;
            ans = std::max(ans, j - i + 1);
        }
        return ans;
    }
};
