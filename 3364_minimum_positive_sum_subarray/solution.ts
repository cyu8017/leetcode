// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

export function minimumSumSubarray(nums: any, l: any, r: any): any {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    let ans = 2147483647;
    let found = false;
    for (let i = 0; i < n; i++) {
        for (let length = l; length <= r && i + length <= n; length++) {
            const s = pref[i + length] - pref[i];
            if (s > 0 && s < ans) {
                ans = s;
                found = true;
            }
        }
    }
    return found ? ans : -1;
}
