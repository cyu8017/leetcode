// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

export function minCost(startPos: number[], homePos: number[], rowCosts: number[], colCosts: number[]): number {
    let ans = 0;
    const sr = startPos[0], sc = startPos[1], hr = homePos[0], hc = homePos[1];
    if (sr < hr) for (let r = sr + 1; r <= hr; r++) ans += rowCosts[r];
    else for (let r = sr - 1; r >= hr; r--) ans += rowCosts[r];
    if (sc < hc) for (let c = sc + 1; c <= hc; c++) ans += colCosts[c];
    else for (let c = sc - 1; c >= hc; c--) ans += colCosts[c];
    return ans;
}
