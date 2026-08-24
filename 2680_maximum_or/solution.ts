// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

export function maximumOr(nums: any, k: any): any {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    const suf = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] | nums[i];
    for (let i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] | nums[i];
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const cur = pref[i] | (nums[i] * (2 ** k)) | suf[i + 1];
        if (cur > ans) ans = cur;
    }
    return ans;
}
