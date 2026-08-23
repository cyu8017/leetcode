// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> minDistinctFreqPair(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int v : nums) cnt[v]++;
        int x = *std::min_element(nums.begin(), nums.end());
        int minY = INT_MAX;
        for (auto& [y, _] : cnt) {
            if (y < minY && cnt[x] != cnt[y]) minY = y;
        }
        if (minY == INT_MAX) return {-1, -1};
        return {x, minY};
    }
};
