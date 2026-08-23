// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var separateDigits = function(nums) {
    const ans = [];
    for (let num of nums) {
        const digits = [];
        while (num > 0) {
            digits.push(num % 10);
            num = Math.floor(num / 10);
        }
        for (let i = digits.length - 1; i >= 0; --i) ans.push(digits[i]);
    }
    return ans;
};
