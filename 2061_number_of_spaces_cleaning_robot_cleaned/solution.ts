// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

export function numberOfCleanRooms(room: number[][]): number {
    const m = room.length, n = room[0].length;
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const vis = new Set();
    const cleaned = new Set([0n]);
    let r = 0, c = 0, d = 0;
    while (true) {
        const state = r * 10000 + c * 10 + d;
        if (vis.has(state)) break;
        vis.add(state);
        const nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] === 0) {
            r = nr; c = nc;
            cleaned.add((BigInt(r) << 32n) ^ (BigInt(c) & 0xffffffffn));
        } else d = (d + 1) % 4;
    }
    return cleaned.size;
}
