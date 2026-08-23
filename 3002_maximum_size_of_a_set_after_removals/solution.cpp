// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maximumSetSize(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> s1(nums1.begin(), nums1.end());
        std::unordered_set<int> s2(nums2.begin(), nums2.end());
        int a = 0, b = 0, c = 0;
        for (int x : s1) if (!s2.count(x)) a++;
        for (int x : s2) {
            if (!s1.count(x)) b++;
            else c++;
        }
        int n = (int)nums1.size();
        a = std::min(a, n / 2);
        b = std::min(b, n / 2);
        return std::min(a + b + c, n);
    }
};
