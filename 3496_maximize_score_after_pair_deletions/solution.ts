// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

export function maximizeScore(nums: any): any {
    const n = nums.length;
    let total = 0;
    for (const x of nums) total += x;
    if (n % 2 === 1) {
        let mn = nums[0];
        for (const x of nums) if (x < mn) mn = x;
        return total - mn;
    }
    let mn = nums[0] + nums[1];
    for (let i = 0; i + 1 < n; i++) mn = Math.min(mn, nums[i] + nums[i + 1]);
    return total - mn;
}
