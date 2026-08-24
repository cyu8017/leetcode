// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

export function minimumLevels(possible: number[]): number {
    let s = 0;
    for (const x of possible) s += (x === 0 ? -1 : x);
    let t = 0;
    for (let i = 0; i + 1 < possible.length; i++) {
        const x = possible[i] === 0 ? -1 : possible[i];
        t += x;
        if (t > s - t) return i + 1;
    }
    return -1;
}
