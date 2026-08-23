// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::vector<int> map(std::vector<int>& arr, std::function<int(int, int)> fn) {
        std::vector<int> out(arr.size());
        for (int i = 0; i < (int)arr.size(); ++i) out[i] = fn(arr[i], i);
        return out;
    }
};
