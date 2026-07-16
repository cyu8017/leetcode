// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

export function removeDuplicates(nums: number[]): number {
    if (nums.length <= 2) {
        return nums.length;
    }

    let write = 2;
    for (let i = 2; i < nums.length; i++) {
        if (nums[i] !== nums[write - 2]) {
            nums[write] = nums[i];
            write++;
        }
    }

    return write;
}
