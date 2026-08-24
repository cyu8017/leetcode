// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

export function answerQueries(nums: number[], queries: number[]): number[] {
    nums = nums.slice().sort((a, b) => a - b);
    for (let i = 1; i < nums.length; i++) nums[i] += nums[i - 1];
    const ans = Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let lo = 0, hi = nums.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (nums[mid] <= queries[i]) lo = mid + 1;
            else hi = mid;
        }
        ans[i] = lo;
    }
    return ans;
}
