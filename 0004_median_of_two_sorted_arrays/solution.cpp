// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            std::swap(nums1, nums2);
        }

        int m = static_cast<int>(nums1.size());
        int n = static_cast<int>(nums2.size());
        int totalLeft = (m + n + 1) / 2;
        int lo = 0;
        int hi = m;

        while (lo <= hi) {
            int i = (lo + hi) / 2;
            int j = totalLeft - i;

            int nums1LeftMax = i == 0 ? INT_MIN : nums1[i - 1];
            int nums1RightMin = i == m ? INT_MAX : nums1[i];
            int nums2LeftMax = j == 0 ? INT_MIN : nums2[j - 1];
            int nums2RightMin = j == n ? INT_MAX : nums2[j];

            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
                if ((m + n) % 2 == 1) {
                    return static_cast<double>(std::max(nums1LeftMax, nums2LeftMax));
                }
                return (std::max(nums1LeftMax, nums2LeftMax) + std::min(nums1RightMin, nums2RightMin)) / 2.0;
            }

            if (nums1LeftMax > nums2RightMin) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }

        return 0.0;
    }
};
