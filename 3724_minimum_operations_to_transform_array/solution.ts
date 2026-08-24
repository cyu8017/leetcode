// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

export function minOperations(nums1: any, nums2: any): any {
    let ans = 1;
    const n = nums1.length;
    let ok = false;
    let d = 1 << 30;
    for (let i = 0; i < n; i++) {
        const x = Math.max(nums1[i], nums2[i]);
        const y = Math.min(nums1[i], nums2[i]);
        ans += x - y;
        d = Math.min(d, Math.min(Math.abs(x - nums2[n]), Math.abs(y - nums2[n])));
        if (nums2[n] >= y && nums2[n] <= x) ok = true;
    }
    if (!ok) ans += d;
    return ans;
}
