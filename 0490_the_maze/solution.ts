// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

export class Solution {
    hasPath(maze: number[][], start: number[], destination: number[]): boolean {
        const rows = maze.length;
        const cols = maze[0].length;
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        const visited = new Set<string>();
        const stack: number[][] = [[start[0], start[1]]];

        while (stack.length) {
            const [row, col] = stack.pop() as number[];
            const key = `${row},${col}`;
            if (visited.has(key)) continue;
            visited.add(key);
            if (row === destination[0] && col === destination[1]) return true;
            for (const [dr, dc] of directions) {
                let nr = row;
                let nc = col;
                while (nr + dr >= 0 && nr + dr < rows && nc + dc >= 0 && nc + dc < cols && maze[nr + dr][nc + dc] === 0) {
                    nr += dr;
                    nc += dc;
                }
                const nextKey = `${nr},${nc}`;
                if (!visited.has(nextKey)) stack.push([nr, nc]);
            }
        }
        return false;
    }
}
