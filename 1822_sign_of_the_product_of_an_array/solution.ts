// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

function arraySign(nums: number[]): number {
    let sign = 1;
    for (const num of nums) {
        if (num === 0) return 0;
        if (num < 0) sign = -sign;
    }
    return sign;
}
