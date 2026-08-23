// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/
// JS-only problem; C++ stand-in.

#include <functional>
#include <vector>

class Solution {
public:
    void forEach(std::vector<int>& arr, std::function<void(int, int, std::vector<int>&)> callback) {
        for (int i = 0; i < (int)arr.size(); i++) callback(arr[i], i, arr);
    }
};
