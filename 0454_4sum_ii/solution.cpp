// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int fourSumCount(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<int>& nums3,
                     std::vector<int>& nums4) {
        std::unordered_map<int, int> pairSums;
        for (int a : nums1) {
            for (int b : nums2) {
                ++pairSums[a + b];
            }
        }

        int total = 0;
        for (int c : nums3) {
            for (int d : nums4) {
                total += pairSums[-(c + d)];
            }
        }
        return total;
    }
};
