// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> numberOfPairs(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        int pairs = 0, left = 0;
        for (auto& [_, c] : cnt) {
            pairs += c / 2;
            left += c % 2;
        }
        return {pairs, left};
    }
};
