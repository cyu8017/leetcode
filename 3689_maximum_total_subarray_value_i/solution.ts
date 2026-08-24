// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

export function maxTotalValue(nums: any, k: any): any {
    let mn = nums[0], mx = nums[0];
    for (const x of nums) {
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
    }
    return k * (mx - mn);
}
