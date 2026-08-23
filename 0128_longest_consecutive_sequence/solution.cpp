// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

#include <vector>
#include <unordered_set>
#include <algorithm>
class Solution { public: int longestConsecutive(std::vector<int>& nums) {
    std::unordered_set<int> values(nums.begin(), nums.end()); int best = 0;
    for (int value : values) if (!values.count(value - 1)) { int length = 1; while (values.count(value + length)) ++length; best = std::max(best, length); }
    return best;
} };