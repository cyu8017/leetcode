// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

function equal(a: any, as: any, ae: any, b: any, bs: any, be: any): any {
    if (ae - as !== be - bs) return false;
    for (let i = 0; i < ae - as; i++) if (a[as + i] !== b[bs + i]) return false;
    return true;
}export function beautifulSplits(nums: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 1; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            let ok = false;
            if (i <= j - i && equal(nums, 0, i, nums, i, i + i)) ok = true;
            if (!ok && j - i <= n - j && equal(nums, i, j, nums, j, j + (j - i))) ok = true;
            if (ok) ans++;
        }
    }
    return ans;
}
