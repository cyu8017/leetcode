// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> findIntersectionValues(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> s1(nums1.begin(), nums1.end()), s2(nums2.begin(), nums2.end());
        int a = 0, b = 0;
        for (int v : nums1) if (s2.count(v)) a++;
        for (int v : nums2) if (s1.count(v)) b++;
        return {a, b};
    }
};
