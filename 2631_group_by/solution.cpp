// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

#include <functional>
#include <string>
#include <unordered_map>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::unordered_map<std::string, std::vector<int>> groupBy(std::vector<int>& arr, std::function<std::string(int)> fn) {
        std::unordered_map<std::string, std::vector<int>> out;
        for (int x : arr) out[fn(x)].push_back(x);
        return out;
    }
};
