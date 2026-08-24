// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

function bitLen(x: any): any {
    if (x === 0) return 0;
    let n = 0;
    while (x > 0) { n++; x >>= 1; }
    return n;
}export function minimumOR(grid: any): any {
    let mx = 0;
    for (const row of grid) for (const x of row) mx = Math.max(mx, x);
    const m = bitLen(mx);
    let ans = 0;
    for (let i = m - 1; i >= 0; i--) {
        const mask = ans | ((1 << i) - 1);
        for (const row of grid) {
            let found = false;
            for (const x of row) {
                if ((x | mask) === mask) { found = true; break; }
            }
            if (!found) {
                ans |= 1 << i;
                break;
            }
        }
    }
    return ans;
}
