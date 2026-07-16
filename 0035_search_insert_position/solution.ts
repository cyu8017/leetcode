// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

export function searchInsert(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}
