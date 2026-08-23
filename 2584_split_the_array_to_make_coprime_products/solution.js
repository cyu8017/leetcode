// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findValidSplit = function(nums) {
    const first = new Map(), last = new Map();
    const factorize = (x, idx) => {
        for (let p = 2; p * p <= x; ++p) {
            if (x % p === 0) {
                if (!first.has(p)) first.set(p, idx);
                last.set(p, idx);
                while (x % p === 0) x = Math.floor(x / p);
            }
        }
        if (x > 1) {
            if (!first.has(x)) first.set(x, idx);
            last.set(x, idx);
        }
    };
    const n = nums.length;
    for (let i = 0; i < n; ++i) factorize(nums[i], i);
    let far = 0;
    for (let i = 0; i < n - 1; ++i) {
        let x = nums[i];
        for (let p = 2; p * p <= x; ++p) {
            if (x % p === 0) {
                if (last.get(p) > far) far = last.get(p);
                while (x % p === 0) x = Math.floor(x / p);
            }
        }
        if (x > 1 && last.get(x) > far) far = last.get(x);
        if (far === i) return i;
    }
    return -1;
};
