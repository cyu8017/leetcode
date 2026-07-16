// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

export class Solution {
    predictTheWinner(nums: number[]): boolean {
        const n = nums.length;
        const dp = Array.from({ length: n }, () => Array<number>(n).fill(0));
        for (let i = 0; i < n; i += 1) dp[i][i] = nums[i];
        for (let length = 2; length <= n; length += 1) {
            for (let left = 0; left <= n - length; left += 1) {
                const right = left + length - 1;
                dp[left][right] = Math.max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1]);
            }
        }
        return dp[0][n - 1] >= 0;
    }
}
