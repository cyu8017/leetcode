// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

#include <vector>

class NumArray {
    std::vector<int> nums;
    std::vector<int> tree;
    int size;

    void add(int index, int delta) {
        while (index <= size) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int prefix(int index) const {
        int total = 0;
        while (index > 0) {
            total += tree[index];
            index -= index & -index;
        }
        return total;
    }

public:
    NumArray(std::vector<int>& nums) : nums(nums), size(static_cast<int>(nums.size())), tree(size + 1, 0) {
        for (int index = 0; index < size; index++) {
            add(index + 1, nums[index]);
        }
    }

    void update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        add(index + 1, delta);
    }

    int sumRange(int left, int right) {
        return prefix(right + 1) - prefix(left);
    }
};
