// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

export function maxScore(nums: any): any {
    const n = nums.length;
    const f = new Array(n).fill(0);
    const dfs = (i) => {
        if (f[i] > 0) return f[i];
        for (let j = i + 1; j < n; j++) f[i] = Math.max(f[i], (j - i) * nums[j] + dfs(j));
        return f[i];
    };
    return dfs(0);
}
