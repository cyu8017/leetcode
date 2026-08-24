// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

export function countMaxOrSubsets(nums: number[]): number {
    let maxOr = 0, ans = 0;
    for (const x of nums) maxOr |= x;
    const dfs = (i, cur) => {
        if (i === nums.length) { if (cur === maxOr) ans++; return; }
        dfs(i + 1, cur);
        dfs(i + 1, cur | nums[i]);
    };
    dfs(0, 0);
    return ans;
}
