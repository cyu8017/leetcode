// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

export function missingRolls(rolls: number[], mean: number, n: number): number[] {
    let sum = 0;
    for (const r of rolls) sum += r;
    const remain = mean * (rolls.length + n) - sum;
    if (remain < n || remain > 6 * n) return [];
    const ans = new Array(n);
    const baseVal = Math.floor(remain / n), extra = remain % n;
    for (let i = 0; i < n; i++) ans[i] = baseVal + (i < extra ? 1 : 0);
    return ans;
}
