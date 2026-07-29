// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minSwap(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = static_cast<int>(nums1.size());
        std::vector<int> swap(n, n), keep(n, n);
        swap[0] = 1;
        keep[0] = 0;
        for (int i = 1; i < n; ++i) {
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                keep[i] = keep[i - 1];
                swap[i] = swap[i - 1] + 1;
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                keep[i] = std::min(keep[i], swap[i - 1]);
                swap[i] = std::min(swap[i], keep[i - 1] + 1);
            }
        }
        return std::min(swap[n - 1], keep[n - 1]);
    }
};
