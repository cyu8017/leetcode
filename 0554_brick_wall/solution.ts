// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

export function leastBricks(wall: number[][]): number {
    const edges = new Map();
    let best = 0;
    for (const row of wall) {
        let width = 0;
        for (let i = 0; i + 1 < row.length; ++i) {
            width += row[i];
            const count = (edges.get(width) || 0) + 1;
            edges.set(width, count);
            best = Math.max(best, count);
        }
    }
    return wall.length - best;
}
