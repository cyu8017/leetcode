// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

export function numberOfArrays(differences: number[], lower: number, upper: number): number {
    let cur = 0, mn = 0, mx = 0;
    for (const d of differences) {
        cur += d;
        mn = Math.min(mn, cur);
        mx = Math.max(mx, cur);
    }
    const res = (upper - lower) - (mx - mn) + 1;
    return res < 0 ? 0 : res;
}
