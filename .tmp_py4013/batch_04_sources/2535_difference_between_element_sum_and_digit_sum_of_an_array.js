// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    let elem = 0, digit = 0;
    for (let num of nums) {
        elem += num;
        let x = num;
        while (x > 0) {
            digit += x % 10;
            x = Math.floor(x / 10);
        }
    }
    return Math.abs(elem - digit);
};
