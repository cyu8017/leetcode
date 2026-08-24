// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

export function minimumCost(s: any): any {
    const n = s.length;
    let ans = 0;
    for (let i = 1; i < n; i++) {
        if (s[i] !== s[i - 1]) ans += Math.min(i, n - i);
    }
    return ans;
}
