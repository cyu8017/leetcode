// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> getFinalState(std::vector<int>& nums, int k, int multiplier) {
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> h;
        for (int i = 0; i < (int)nums.size(); i++) h.push({nums[i], i});
        for (int t = 0; t < k; t++) {
            auto [v, i] = h.top();
            h.pop();
            v *= multiplier;
            nums[i] = v;
            h.push({v, i});
        }
        return nums;
    }
};
