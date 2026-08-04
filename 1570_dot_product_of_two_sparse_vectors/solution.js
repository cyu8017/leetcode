// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

/**
 * @param {number[]} nums
 * @return {SparseVector}
 */
var SparseVector = function(nums) {
    this.values = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) this.values.set(i, nums[i]);
    }
};

/**
 * @param {SparseVector} vec
 * @return {number}
 */
SparseVector.prototype.dotProduct = function(vec) {
    if (this.values.size > vec.values.size) return vec.dotProduct(this);
    let sum = 0;
    for (const [i, x] of this.values) {
        if (vec.values.has(i)) sum += x * vec.values.get(i);
    }
    return sum;
};

/**
 * Compatibility wrapper for local tests that call a function.
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var dotProduct = function(nums1, nums2) {
    return new SparseVector(nums1).dotProduct(new SparseVector(nums2));
};
