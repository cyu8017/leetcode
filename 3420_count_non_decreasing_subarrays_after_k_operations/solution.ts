// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

export function countNonDecreasingSubarrays(nums: any, k: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let cost = 0;
        let maxV = nums[i];
        for (let j = i; j < n; j++) {
            if (nums[j] >= maxV) maxV = nums[j];
            else cost += maxV - nums[j];
            if (cost > k) break;
            ans++;
        }
    }
    return ans;
}
