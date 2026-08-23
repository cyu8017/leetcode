// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

#include <vector>
#include <algorithm>

class Solution {
public:
    int addedInteger(std::vector<int>& nums1, std::vector<int>& nums2) {
        return *std::min_element(nums2.begin(), nums2.end()) -
               *std::min_element(nums1.begin(), nums1.end());
    }
};
