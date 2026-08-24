// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

export function maximizeGreatness(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let i = 0;
    for (const x of nums) {
        if (x > nums[i]) i++;
    }
    return i;
}
