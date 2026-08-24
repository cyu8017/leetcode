// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

export function evenNumberBitwiseORs(nums: any): any {
    let ans = 0;
    for (const x of nums) if (x % 2 === 0) ans |= x;
    return ans;
}
