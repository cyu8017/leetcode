// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

export function transformArray(nums: any): any {
    for (let i = 0; i < nums.length; i++) nums[i] %= 2;
    let j = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            const t = nums[i]; nums[i] = nums[j]; nums[j] = t;
            j++;
        }
    }
    return nums;
}
