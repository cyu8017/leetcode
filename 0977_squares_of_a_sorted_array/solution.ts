// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

export function sortedSquares(nums: number[]): number[] {
    const n = nums.length;
    const ans = new Array(n);
    let i = 0, j = n - 1;
    for (let k = n - 1; k >= 0; k--) {
        if (Math.abs(nums[i]) > Math.abs(nums[j])) {
            ans[k] = nums[i] * nums[i];
            i++;
        } else {
            ans[k] = nums[j] * nums[j];
            j--;
        }
    }
    return ans;
}
