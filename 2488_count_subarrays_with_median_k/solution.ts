// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

export function countSubarrays(nums: number[], k: number): number {
    let pos = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === k) { pos = i; break; }
    }
    const bal = new Map();
    bal.set(0, 1);
    let cur = 0;
    for (let i = pos - 1; i >= 0; i--) {
        cur += nums[i] < k ? -1 : 1;
        bal.set(cur, (bal.get(cur) || 0) + 1);
    }
    let ans = (bal.get(0) || 0) + (bal.get(1) || 0);
    cur = 0;
    for (let i = pos + 1; i < nums.length; i++) {
        cur += nums[i] < k ? -1 : 1;
        ans += (bal.get(-cur) || 0) + (bal.get(1 - cur) || 0);
    }
    return ans;
}
