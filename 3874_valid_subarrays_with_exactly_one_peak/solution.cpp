// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long validSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> peaks;
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) peaks.push_back(i);
        }
        int64_t ans = 0;
        for (int j = 0; j < (int)peaks.size(); j++) {
            int p = peaks[j];
            int leftMin = std::max(p - k, 0);
            if (j > 0) leftMin = std::max(leftMin, peaks[j - 1] + 1);
            int rightMax = std::min(p + k, n - 1);
            if (j < (int)peaks.size() - 1) rightMax = std::min(rightMax, peaks[j + 1] - 1);
            ans += (int64_t)(p - leftMin + 1) * (rightMax - p + 1);
        }
        return ans;
    }
};
