// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums1, std::vector<int>& nums2) {
        if ((int)nums1.size() * 6 < (int)nums2.size() ||
            (int)nums2.size() * 6 < (int)nums1.size()) {
            return -1;
        }
        int s1 = std::accumulate(nums1.begin(), nums1.end(), 0);
        int s2 = std::accumulate(nums2.begin(), nums2.end(), 0);
        if (s1 == s2) {
            return 0;
        }
        const std::vector<int>* big = &nums1;
        const std::vector<int>* small = &nums2;
        if (s1 < s2) {
            std::swap(big, small);
            std::swap(s1, s2);
        }
        int diff = s1 - s2;
        std::vector<int> gains;
        gains.reserve(big->size() + small->size());
        for (int x : *big) {
            gains.push_back(x - 1);
        }
        for (int x : *small) {
            gains.push_back(6 - x);
        }
        std::sort(gains.begin(), gains.end(), std::greater<int>());
        int ops = 0;
        for (int gain : gains) {
            if (diff <= 0) {
                break;
            }
            diff -= gain;
            ops++;
        }
        return diff <= 0 ? ops : -1;
    }
};
