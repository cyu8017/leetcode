// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

function isGoodArray(nums: number[]): boolean {
    let g = nums[0];
    for (let i = 1; i < nums.length; i++) g = gcd(g, nums[i]);
    return g === 1;
}
