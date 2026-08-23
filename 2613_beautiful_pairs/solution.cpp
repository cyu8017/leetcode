// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> beautifulPair(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        long long bestDist = (long long)1e18;
        std::vector<int> ans = {0, 1};
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long d = std::abs(nums1[i] - nums1[j]) + std::abs(nums2[i] - nums2[j]);
                if (d < bestDist || (d == bestDist && (i < ans[0] || (i == ans[0] && j < ans[1])))) {
                    bestDist = d;
                    ans = {i, j};
                }
            }
        }
        return ans;
    }
};
