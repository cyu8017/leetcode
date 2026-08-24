// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

export function maxScore(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let sum = 0, ans = 0;
    for (let i = nums.length - 1; i >= 0; --i) {
        sum += nums[i];
        if (sum > 0) ans++;
        else break;
    }
    return ans;
}
