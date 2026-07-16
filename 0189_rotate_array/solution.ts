// LeetCode 0189 - Rotate Array
// https://leetcode.com/problems/rotate-array/

export function rotate(nums: number[], k: number): void {
    const reverse = (left: number, right: number): void => {
        while (left < right) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            left++;
            right--;
        }
    };

    k %= nums.length;
    reverse(0, nums.length - 1);
    reverse(0, k - 1);
    reverse(k, nums.length - 1);
}