// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/
// JS-only problem; C++ vector filter stand-in.

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> deepFilter(std::vector<int>& obj, std::function<bool(int)> fn) {
        std::vector<int> out;
        for (int v : obj) if (fn(v)) out.push_back(v);
        return out;
    }
};
