"use strict";
// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
// @ts-nocheck
function numTriplets(nums1, nums2) {
    const count = (a, b) => {
        const squares = new Map();
        for (const x of a) {
            const sq = x * x;
            squares.set(sq, (squares.get(sq) || 0) + 1);
        }
        const products = new Map();
        for (let i = 0; i < b.length; i++) {
            for (let j = i + 1; j < b.length; j++) {
                const p = b[i] * b[j];
                products.set(p, (products.get(p) || 0) + 1);
            }
        }
        let ans = 0;
        for (const [value, c] of squares)
            ans += c * (products.get(value) || 0);
        return ans;
    };
    return count(nums1, nums2) + count(nums2, nums1);
}
