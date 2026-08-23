// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::vector<int> filter(std::vector<int>& arr, std::function<bool(int, int)> fn) {
        std::vector<int> out;
        for (int i = 0; i < (int)arr.size(); ++i) {
            if (fn(arr[i], i)) out.push_back(arr[i]);
        }
        return out;
    }
};
