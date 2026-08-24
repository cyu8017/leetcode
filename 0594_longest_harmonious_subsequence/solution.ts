// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

export function findLHS(nums: number[]): number {
    const counts = new Map();
    for (const num of nums) counts.set(num, (counts.get(num) || 0) + 1);
    let best = 0;
    for (const [key, value] of counts) {
        if (counts.has(key + 1)) best = Math.max(best, value + counts.get(key + 1));
    }
    return best;
}
