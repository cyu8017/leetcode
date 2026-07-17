// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

function solve(nums: number[], queries: number[][]): number[] {
    const mod = 1000000007;
    const n = nums.length;
    const block = Math.floor(Math.sqrt(n)) + 1;
    const dp: number[][] = Array.from({ length: block }, () => new Array(n).fill(0));
    for (let step = 1; step < block; step++) {
        for (let i = n - 1; i >= 0; i--) {
            dp[step][i] = (nums[i] + (i + step < n ? dp[step][i + step] : 0)) % mod;
        }
    }
    const ans: number[] = [];
    for (const [start, step] of queries) {
        if (step < block) {
            ans.push(dp[step][start]);
        } else {
            let total = 0;
            for (let i = start; i < n; i += step) {
                total += nums[i];
            }
            ans.push(total % mod);
        }
    }
    return ans;
}
