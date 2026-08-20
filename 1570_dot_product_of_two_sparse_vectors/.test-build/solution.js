"use strict";
// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
// @ts-nocheck
Object.defineProperty(exports, "__esModule", { value: true });
exports.SparseVector = void 0;
class SparseVector {
    constructor(nums) {
        this.values = new Map();
        for (let i = 0; i < nums.length; i++) {
            if (nums[i])
                this.values.set(i, nums[i]);
        }
    }
    dotProduct(vec) {
        if (this.values.size > vec.values.size)
            return vec.dotProduct(this);
        let sum = 0;
        for (const [i, x] of this.values) {
            if (vec.values.has(i))
                sum += x * vec.values.get(i);
        }
        return sum;
    }
}
exports.SparseVector = SparseVector;
function dotProduct(nums1, nums2) {
    return new SparseVector(nums1).dotProduct(new SparseVector(nums2));
}
