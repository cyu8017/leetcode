// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minLengthAfterRemovals(std::vector<int>& nums) {
        int n = (int)nums.size(), mx = 0;
        std::unordered_map<int, int> freq;
        for (int v : nums) mx = std::max(mx, ++freq[v]);
        if (mx <= n / 2) return n % 2;
        return 2 * mx - n;
    }
};
