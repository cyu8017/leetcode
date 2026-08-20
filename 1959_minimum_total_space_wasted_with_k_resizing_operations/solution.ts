// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

function minSpaceWastedKResizing(nums: number[], k: number): number {
    const n = nums.length;
    const INF = Number.MAX_SAFE_INTEGER;
    const waste = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        let mx = 0, total = 0;
        for (let j = i; j < n; j++) {
            mx = Math.max(mx, nums[j]);
            total += nums[j];
            waste[i][j] = mx * (j - i + 1) - total;
        }
    }
    const segments = k + 1;
    const dp = Array.from({ length: n + 1 }, () => new Array(segments + 1).fill(INF));
    dp[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let s = 1; s <= Math.min(segments, i); s++) {
            for (let p = s - 1; p < i; p++) {
                dp[i][s] = Math.min(dp[i][s], dp[p][s - 1] + waste[p][i - 1]);
            }
        }
    }
    let ans = INF;
    for (let s = 1; s <= segments; s++) ans = Math.min(ans, dp[n][s]);
    return ans;
}
