// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<int>& nums1, std::vector<int>& nums2) {
        int answer = 0;
        int j = 0;
        for (int i = 0; i < static_cast<int>(nums1.size()); i++) {
            while (j < static_cast<int>(nums2.size()) && nums1[i] <= nums2[j]) {
                j++;
            }
            answer = std::max(answer, j - i - 1);
        }
        return answer;
    }
};
