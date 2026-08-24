// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

export function minimumCost(s: any, t: any, flipCost: any, swapCost: any, crossCost: any): any {
    const diff = [0, 0];
    const n = s.length;
    for (let i = 0; i < n; i++) {
        if (s[i] !== t[i]) diff[s.charCodeAt(i) - 48]++;
    }
    let ans = (diff[0] + diff[1]) * flipCost;
    const mx = Math.max(diff[0], diff[1]);
    const mn = Math.min(diff[0], diff[1]);
    ans = Math.min(ans, mn * swapCost + (mx - mn) * flipCost);
    const avg = Math.floor((mx + mn) / 2);
    ans = Math.min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost);
    return ans;
}
