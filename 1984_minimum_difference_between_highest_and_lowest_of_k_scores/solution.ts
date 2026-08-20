// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

function minimumDifference(nums: number[], k: number): number {
    nums = nums.slice().sort((a, b: any) => a - b);
    let ans = Infinity;
    for (let i = 0; i + k - 1 < nums.length; i++) ans = Math.min(ans, nums[i + k - 1] - nums[i]);
    return ans;
}
