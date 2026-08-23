// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<long long> mergeAdjacent(std::vector<int>& nums) {
        std::vector<int64_t> stk;
        for (int x : nums) {
            stk.push_back(x);
            while (stk.size() > 1 && stk.back() == stk[stk.size() - 2]) {
                int64_t a = stk.back();
                stk.pop_back();
                int64_t b = stk.back();
                stk.pop_back();
                stk.push_back(a + b);
            }
        }
        return std::vector<long long>(stk.begin(), stk.end());
    }
};
