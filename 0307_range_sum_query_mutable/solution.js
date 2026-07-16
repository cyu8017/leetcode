// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

class NumArray {
    /**
     * @param {number[]} nums
     */
    constructor(nums) {
        this.nums = nums;
        this.size = nums.length;
        this.tree = Array(this.size + 1).fill(0);
        this.add = (index, delta) => {
            while (index <= this.size) {
                this.tree[index] += delta;
                index += index & -index;
            }
        };
        for (let index = 0; index < nums.length; index += 1) {
            this.add(index + 1, nums[index]);
        }
    }

    /**
     * @param {number} index
     * @param {number} val
     * @return {void}
     */
    update(index, val) {
        const delta = val - this.nums[index];
        this.nums[index] = val;
        this.add(index + 1, delta);
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {number}
     */
    sumRange(left, right) {
        const prefix = (index) => {
            let total = 0;
            while (index > 0) {
                total += this.tree[index];
                index -= index & -index;
            }
            return total;
        };
        return prefix(right + 1) - prefix(left);
    }
}

module.exports = { NumArray };
