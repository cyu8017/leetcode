// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

#include <vector>

class NumArray {
    std::vector<int> prefix;

public:
    NumArray(std::vector<int>& nums) {
        prefix.push_back(0);
        for (int num : nums) {
            prefix.push_back(prefix.back() + num);
        }
    }

    int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
};
