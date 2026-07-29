// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::size_t i = 0;
        std::size_t j = 0;
        long long first = 0;
        long long second = 0;
        while (i < nums1.size() || j < nums2.size()) {
            if (j == nums2.size() || (i < nums1.size() && nums1[i] < nums2[j])) {
                first += nums1[i];
                i += 1;
            } else if (i == nums1.size() || nums2[j] < nums1[i]) {
                second += nums2[j];
                j += 1;
            } else {
                first = second = std::max(first, second) + nums1[i];
                i += 1;
                j += 1;
            }
        }
        return static_cast<int>(std::max(first, second) % 1000000007);
    }
};
