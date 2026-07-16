// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

class NumArray {
    /**
     * @param {number[]} nums
     */
    constructor(nums) {
        this.prefix = [0];
        for (const num of nums) {
            this.prefix.push(this.prefix[this.prefix.length - 1] + num);
        }
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {number}
     */
    sumRange(left, right) {
        return this.prefix[right + 1] - this.prefix[left];
    }
}

module.exports = { NumArray };
