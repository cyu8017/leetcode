// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

export function maximumScore(nums: any): any {
    const n = nums.length;
    const suf = new Array(n);
    suf[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) suf[i] = Math.min(nums[i], suf[i + 1]);
    let pre = 0;
    let ans = Number.MIN_SAFE_INTEGER;
    for (let i = 0; i < n - 1; i++) {
        pre += nums[i];
        ans = Math.max(ans, pre - suf[i + 1]);
    }
    return ans;
}
