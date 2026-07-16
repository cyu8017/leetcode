// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

export function moveZeroes(nums: number[]): void {
    let insert = 0;
    for (const num of nums) {
        if (num !== 0) {
            nums[insert] = num;
            insert += 1;
        }
    }
    for (let index = insert; index < nums.length; index += 1) {
        nums[index] = 0;
    }
}
