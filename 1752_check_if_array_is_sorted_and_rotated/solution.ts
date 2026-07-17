// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

function check(nums: number[]): boolean {
    const n = nums.length;
    let drops = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] > nums[(i + 1) % n]) {
            drops++;
        }
    }
    return drops <= 1;
}
