// LeetCode 1929 - Concatenation of Array
// https://leetcode.com/problems/concatenation-of-array/

#include <vector>

class Solution {
public:
    std::vector<int> getConcatenation(std::vector<int>& nums) {
        std::vector<int> res = nums;
        res.insert(res.end(), nums.begin(), nums.end());
        return res;
    }
};
