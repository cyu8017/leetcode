// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

export function maxSum(nums: any, m: any, l: any, r: any): any {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    let dp = new Array(n + 1).fill(0);
    let bestSelected = -(2 ** 62);
    for (let count = 1; count <= m; count++) {
        const next = dp.slice();
        const deque = [];
        for (let end = 1; end <= n; end++) {
            const addIndex = end - l;
            if (addIndex >= 0) {
                const value = dp[addIndex] - prefix[addIndex];
                while (deque.length > 0) {
                    const last = deque[deque.length - 1];
                    if (dp[last] - prefix[last] > value) break;
                    deque.pop();
                }
                deque.push(addIndex);
            }
            const minIndex = end - r;
            while (deque.length > 0 && deque[0] < minIndex) deque.shift();
            if (deque.length > 0) {
                const candidate = prefix[end] + dp[deque[0]] - prefix[deque[0]];
                if (candidate > next[end]) next[end] = candidate;
                if (candidate > bestSelected) bestSelected = candidate;
            }
            if (next[end - 1] > next[end]) next[end] = next[end - 1];
        }
        dp = next;
    }
    return bestSelected;
}
