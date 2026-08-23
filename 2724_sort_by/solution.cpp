// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    // JS sortBy stand-in
    std::vector<int> sortBy(std::vector<int>& arr, std::function<double(int)> fn) {
        std::vector<int> out = arr;
        std::sort(out.begin(), out.end(), [&](int a, int b) { return fn(a) < fn(b); });
        return out;
    }
};
