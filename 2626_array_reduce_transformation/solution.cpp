// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    int reduce(std::vector<int>& nums, std::function<int(int, int)> fn, int init) {
        int acc = init;
        for (int x : nums) acc = fn(acc, x);
        return acc;
    }
};
