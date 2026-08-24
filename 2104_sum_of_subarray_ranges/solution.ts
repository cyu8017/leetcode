// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

export function subArrayRanges(nums: number[]): number {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let mn = nums[i], mx = nums[i];
        for (let j = i; j < n; j++) {
            mn = Math.min(mn, nums[j]);
            mx = Math.max(mx, nums[j]);
            ans += mx - mn;
        }
    }
    return ans;
}
