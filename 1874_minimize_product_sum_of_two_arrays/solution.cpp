// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minProductSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end(), std::greater<int>());
        int answer = 0;
        for (int i = 0; i < static_cast<int>(nums1.size()); i++) {
            answer += nums1[i] * nums2[i];
        }
        return answer;
    }
};
