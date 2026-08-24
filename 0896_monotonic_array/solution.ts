// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

export function isMonotonic(nums: number[]): boolean {
    let inc = true, dec = true;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) inc = false;
        if (nums[i] > nums[i - 1]) dec = false;
    }
    return inc || dec;
}
