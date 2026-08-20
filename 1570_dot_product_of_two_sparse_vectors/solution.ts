// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
// @ts-nocheck

export class SparseVector {
    values: Map<number, number>;

    constructor(nums: number[]) {
        this.values = new Map();
        for (let i = 0; i < nums.length; i++) {
            if (nums[i]) this.values.set(i, nums[i]);
        }
    }

    dotProduct(vec: SparseVector): number {
        if (this.values.size > vec.values.size) return vec.dotProduct(this);
        let sum = 0;
        for (const [i, x] of this.values) {
            if (vec.values.has(i)) sum += x * vec.values.get(i)!;
        }
        return sum;
    }
}

function dotProduct(nums1: number[], nums2: number[]): number {
    return new SparseVector(nums1).dotProduct(new SparseVector(nums2));
}
