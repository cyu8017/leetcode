// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

export function maxValue(n: any, restrictions: any, diff: any): any {
    const INF = Math.floor(2147483647 / 4);
    const bound = new Array(n).fill(INF);
    bound[0] = 0;
    for (const r of restrictions) bound[r[0]] = r[1];
    for (let i = 1; i < n; i++) bound[i] = Math.min(bound[i], bound[i - 1] + diff[i - 1]);
    for (let i = n - 2; i >= 0; i--) bound[i] = Math.min(bound[i], bound[i + 1] + diff[i]);
    let ans = bound[0];
    for (let i = 1; i < n; i++) ans = Math.max(ans, bound[i]);
    return ans;
}
