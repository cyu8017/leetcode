// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

function maxProductDifference(nums: number[]): number {
    let a = 0, b = 0, c = 1e5, d = 1e5;
    for (const x of nums) {
        if (x > a) { b = a; a = x; }
        else if (x > b) b = x;
        if (x < c) { d = c; c = x; }
        else if (x < d) d = x;
    }
    return a * b - c * d;
}
