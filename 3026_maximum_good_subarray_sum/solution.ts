// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

export function maximumSubarraySum(nums: any, k: any): any {
    const p = new Map();
    p.set(nums[0], 0);
    let s = 0;
    const n = nums.length;
    let ans = -Infinity;
    for (let i = 0; i < n; i++) {
        s += nums[i];
        if (p.has(nums[i] - k)) ans = Math.max(ans, s - p.get(nums[i] - k));
        if (p.has(nums[i] + k)) ans = Math.max(ans, s - p.get(nums[i] + k));
        if (i + 1 === n) break;
        const old = p.get(nums[i + 1]);
        if (old === undefined || s < old) p.set(nums[i + 1], s);
    }
    return ans === -Infinity ? 0 : ans;
}
