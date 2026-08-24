// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

export function canSplitArray(nums: number[], m: number): boolean {
    const n = nums.length;
    if (n <= 2) return true;
    for (let i = 0; i + 1 < n; i++) {
        if (nums[i] + nums[i + 1] >= m) return true;
    }
    return false;
}
