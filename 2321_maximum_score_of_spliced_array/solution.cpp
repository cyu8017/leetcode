// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumsSplicedArray(std::vector<int>& nums1, std::vector<int>& nums2) {
        auto kadane = [](const std::vector<int>& a, const std::vector<int>& b) {
            int best = 0, cur = 0, sum = 0;
            for (size_t i = 0; i < a.size(); ++i) {
                sum += a[i];
                cur += b[i] - a[i];
                if (cur < 0) cur = 0;
                best = std::max(best, cur);
            }
            return sum + best;
        };
        return std::max(kadane(nums1, nums2), kadane(nums2, nums1));
    }
};
