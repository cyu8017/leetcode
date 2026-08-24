// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

export function sortArrayByParity(nums: number[]): number[] {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] % 2 === 0) {
            const tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
        }
    }
    return nums;
}
