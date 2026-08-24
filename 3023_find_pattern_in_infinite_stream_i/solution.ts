// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

export function findPattern(stream: any, pattern: any): number {
    let a = 0, b = 0;
    const m = pattern.length;
    const half = m >> 1;
    const mask1 = (1 << half) - 1;
    const mask2 = (1 << (m - half)) - 1;
    for (let i = 0; i < half; i++) a |= pattern[i] << (half - 1 - i);
    for (let i = half; i < m; i++) b |= pattern[i] << (m - 1 - i);
    let x = 0, y = 0;
    for (let i = 1; ; i++) {
        let v = stream.next();
        y = y << 1 | v;
        v = (y >> (m - half)) & 1;
        y &= mask2;
        x = x << 1 | v;
        x &= mask1;
        if (i >= m && a === x && b === y) return i - m;
    }
}
