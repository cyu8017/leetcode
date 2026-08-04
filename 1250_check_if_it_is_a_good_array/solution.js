// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGoodArray = function(nums) {
    let g = nums[0];
    for (let i = 1; i < nums.length; i++) g = gcd(g, nums[i]);
    return g === 1;
};

function gcd(a, b) {
    while (b) [a, b] = [b, a % b];
    return a;
}
