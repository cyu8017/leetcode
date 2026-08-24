// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

export function maximizeWin(prizePositions: number[], k: number): number {
    const n = prizePositions.length;
    const dp = new Array(n + 1).fill(0);
    let ans = 0, left = 0;
    for (let right = 0; right < n; ++right) {
        while (prizePositions[right] - prizePositions[left] > k) left++;
        const cur = right - left + 1;
        if (dp[left] + cur > ans) ans = dp[left] + cur;
        let best = cur;
        if (dp[right] > best) best = dp[right];
        dp[right + 1] = best;
    }
    return ans;
}
