// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxSumAfterOperation(std::vector<int>& nums) {
        long long noSquare = 0;
        long long oneSquare = 0;
        long long best = LLONG_MIN;
        for (int value : nums) {
            long long v = value;
            oneSquare = std::max({oneSquare + v, noSquare + v * v, v * v});
            noSquare = std::max(noSquare + v, v);
            best = std::max(best, oneSquare);
        }
        return static_cast<int>(best);
    }
};
