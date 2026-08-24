// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

export function findMaximumLength(nums: any): any {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    const last = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    const dp = new Array(n + 1).fill(0);
    const dq = [[0, 0]];
    for (let i = 1; i <= n; i++) {
        while (dq.length > 1 && dq[1][1] <= pref[i]) dq.shift();
        const j = dq[0][0];
        dp[i] = dp[j] + 1;
        last[i] = pref[i] - pref[j];
        const val = pref[i] + last[i];
        while (dq.length && dq[dq.length - 1][1] >= val) dq.pop();
        dq.push([i, val]);
    }
    return dp[n];
}
