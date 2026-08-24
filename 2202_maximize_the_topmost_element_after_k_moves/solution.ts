// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

export function maximumTop(nums: number[], k: number): number {
    const n = nums.length;
    if (n === 1) return k % 2 !== 0 ? -1 : nums[0];
    if (k === 0) return nums[0];
    let ans = -1;
    const limit = Math.min(k - 1, n);
    for (let i = 0; i < limit; i++) ans = Math.max(ans, nums[i]);
    if (k < n) ans = Math.max(ans, nums[k]);
    return ans;
}
