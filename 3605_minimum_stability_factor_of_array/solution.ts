// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

function gcd3605(a: any, b: any): any {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}function ok3605(nums: any, maxC: any, x: any): any {
    const n = nums.length;
    if (x >= n) return true;
    let changes = 0, i = 0;
    while (i + x < n) {
        let g = nums[i];
        for (let j = i + 1; j <= i + x; j++) g = gcd3605(g, nums[j]);
        if (g > 1) {
            changes++;
            i += x + 1;
        } else {
            i++;
        }
    }
    return changes <= maxC;
}export function minStable(nums: any, maxC: any): any {
    const n = nums.length;
    let lo = 0, hi = n;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok3605(nums, maxC, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
