// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

export function shortestSubarray(nums: number[], k: number): number {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    const dq = [];
    let ans = n + 1;
    for (let i = 0; i <= n; i++) {
        while (dq.length && prefix[i] - prefix[dq[0]] >= k) {
            ans = Math.min(ans, i - dq.shift());
        }
        while (dq.length && prefix[i] <= prefix[dq[dq.length - 1]]) dq.pop();
        dq.push(i);
    }
    return ans <= n ? ans : -1;
}
