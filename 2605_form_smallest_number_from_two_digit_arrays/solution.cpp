// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minNumber(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> s1(nums1.begin(), nums1.end()), s2(nums2.begin(), nums2.end());
        int bestShared = 10;
        for (int d = 1; d <= 9; ++d) {
            if (s1.count(d) && s2.count(d) && d < bestShared) bestShared = d;
        }
        if (bestShared < 10) return bestShared;
        int m1 = 10, m2 = 10;
        for (int x : nums1) if (x < m1) m1 = x;
        for (int x : nums2) if (x < m2) m2 = x;
        if (m1 < m2) return m1 * 10 + m2;
        return m2 * 10 + m1;
    }
};
