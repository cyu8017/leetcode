// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minCost(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> cnt2;
        for (int x : nums2) cnt2[x]++;
        std::unordered_map<int, int> cnt1;
        for (int x : nums1) {
            if (cnt2[x] > 0) cnt2[x]--;
            else cnt1[x]++;
        }
        int ans = 0;
        for (auto& [_, v] : cnt1) {
            if (v % 2 == 1) return -1;
            ans += v / 2;
        }
        for (auto& [_, v] : cnt2) {
            if (v % 2 == 1) return -1;
        }
        return ans;
    }
};
