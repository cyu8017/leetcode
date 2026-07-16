// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

export class Solution {
    findShortestWay(maze: number[][], ball: number[], hole: number[]): string {
        const rows = maze.length;
        const cols = maze[0].length;
        const holePos = `${hole[0]},${hole[1]}`;
        const directions: Record<string, [number, number]> = {
            d: [1, 0],
            l: [0, -1],
            r: [0, 1],
            u: [-1, 0],
        };

        const roll = (row: number, col: number, dr: number, dc: number): [number, number, number] => {
            let distance = 0;
            while (row + dr >= 0 && row + dr < rows && col + dc >= 0 && col + dc < cols && maze[row + dr][col + dc] === 0) {
                row += dr;
                col += dc;
                distance += 1;
                if (`${row},${col}` === holePos) break;
            }
            return [row, col, distance];
        };

        const best = new Map<string, { dist: number; path: string }>();
        const heap: Array<{ dist: number; path: string; row: number; col: number }> = [
            { dist: 0, path: "", row: ball[0], col: ball[1] },
        ];

        while (heap.length) {
            heap.sort((a, b) => a.dist - b.dist || a.path.localeCompare(b.path));
            const { dist, path, row, col } = heap.shift() as { dist: number; path: string; row: number; col: number };
            const state = `${row},${col}`;
            const current = best.get(state);
            if (current && (current.dist < dist || (current.dist === dist && current.path <= path))) continue;
            best.set(state, { dist, path });
            if (state === holePos) return path;

            for (const [direction, [dr, dc]] of Object.entries(directions)) {
                const [nextRow, nextCol, traveled] = roll(row, col, dr, dc);
                if (nextRow === row && nextCol === col) continue;
                const newDist = dist + traveled;
                const newPath = path + direction;
                const target = `${nextRow},${nextCol}`;
                const existing = best.get(target);
                if (!existing || newDist < existing.dist || (newDist === existing.dist && newPath < existing.path)) {
                    heap.push({ dist: newDist, path: newPath, row: nextRow, col: nextCol });
                }
            }
        }
        return "impossible";
    }
}
