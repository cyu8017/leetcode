// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

export function orArray(nums: any): any {
    const ans = new Array(nums.length - 1);
    for (let i = 1; i < nums.length; i++) ans[i - 1] = nums[i] | nums[i - 1];
    return ans;
}
