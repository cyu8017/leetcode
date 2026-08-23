// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

#include <vector>
#include <algorithm>

class Solution {
    bool countInv(const std::vector<int>& nums, int k, int threshold) {
        std::vector<int> sorted;
        long long inv = 0;
        for (int num : nums) {
            auto left = std::upper_bound(sorted.begin(), sorted.end(), num) - sorted.begin();
            auto right = std::upper_bound(sorted.begin(), sorted.end(), num + threshold) - sorted.begin();
            inv += right - left;
            sorted.insert(std::upper_bound(sorted.begin(), sorted.end(), num), num);
        }
        return inv >= k;
    }
public:
    int minThreshold(std::vector<int>& nums, int k) {
        int mx = 0;
        for (int v : nums) if (v > mx) mx = v;
        int l = 0, r = mx + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (countInv(nums, k, m)) r = m;
            else l = m + 1;
        }
        return l > mx ? -1 : l;
    }
};
