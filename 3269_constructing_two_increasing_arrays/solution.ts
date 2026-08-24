// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

export function minLargest(nums1: any, nums2: any): any {
    const n = nums1.length, m = nums2.length;
    const inf = 1000000000;
    const dp = Array.from({length: n + 1}, () => new Array(m + 1).fill(inf));
    dp[0][0] = 0;
    for (let i = 0; i <= n; i++) {
        for (let j = 0; j <= m; j++) {
            if (dp[i][j] === inf) continue;
            const prev = dp[i][j];
            if (i < n) {
                let need = prev + 1;
                if (nums1[i] === 0) { if (need % 2 !== 0) need++; }
                else { if (need % 2 === 0) need++; }
                if (need < dp[i + 1][j]) dp[i + 1][j] = need;
            }
            if (j < m) {
                let need = prev + 1;
                if (nums2[j] === 0) { if (need % 2 !== 0) need++; }
                else { if (need % 2 === 0) need++; }
                if (need < dp[i][j + 1]) dp[i][j + 1] = need;
            }
        }
    }
    return dp[n][m];
}
