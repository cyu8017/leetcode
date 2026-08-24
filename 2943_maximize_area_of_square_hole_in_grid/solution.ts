// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

function maxGap(bars: any): any {
    if (bars.length === 0) return 1;
    bars.sort((a, b) => a - b);
    let best = 1, cur = 1;
    for (let i = 1; i < bars.length; i++) {
        if (bars[i] === bars[i - 1] + 1) cur++;
        else cur = 1;
        if (cur > best) best = cur;
    }
    return best + 1;
}export function maximizeSquareHoleArea(n: any, m: any, hBars: any, vBars: any): any {
    let side = maxGap(hBars.slice());
    const vs = maxGap(vBars.slice());
    if (vs < side) side = vs;
    return side * side;
}
