// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

#include <vector>

class Solution {
public:
    std::vector<int> beautifulArray(int n) {
        if (n == 1) return {1};
        auto left = beautifulArray((n + 1) / 2);
        auto right = beautifulArray(n / 2);
        std::vector<int> ans;
        for (int x : left) ans.push_back(2 * x - 1);
        for (int x : right) ans.push_back(2 * x);
        return ans;
    }
};
