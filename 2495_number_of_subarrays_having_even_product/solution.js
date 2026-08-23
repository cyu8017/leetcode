// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

/**
 * @param {number[]} nums
 * @return {number}
 */
var evenProduct = function(nums) {
    const n = nums.length;
    const total = n * (n + 1) / 2;
    let oddLen = 0, odd = 0;
    for (const x of nums) {
        if (x % 2 === 1) {
            odd++;
            oddLen += odd;
        } else odd = 0;
    }
    return total - oddLen;
};
