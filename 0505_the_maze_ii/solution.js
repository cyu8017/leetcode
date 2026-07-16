// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

class Solution {
    shortestDistance(maze, start, destination) {
        const rows = maze.length;
        const cols = maze[0].length;
        const target = `${destination[0]},${destination[1]}`;
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        const best = new Map();
        const heap = [{ dist: 0, row: start[0], col: start[1] }];

        while (heap.length) {
            heap.sort((a, b) => a.dist - b.dist);
            const { dist, row, col } = heap.shift();
            const state = `${row},${col}`;
            if (state === target) return dist;
            if (best.has(state) && best.get(state) <= dist) continue;
            best.set(state, dist);
            for (const [dr, dc] of directions) {
                let nextRow = row;
                let nextCol = col;
                let traveled = 0;
                while (nextRow + dr >= 0 && nextRow + dr < rows && nextCol + dc >= 0 && nextCol + dc < cols && maze[nextRow + dr][nextCol + dc] === 0) {
                    nextRow += dr;
                    nextCol += dc;
                    traveled += 1;
                }
                if (nextRow !== row || nextCol !== col) {
                    const newDist = dist + traveled;
                    const nextState = `${nextRow},${nextCol}`;
                    if (!best.has(nextState) || newDist < best.get(nextState)) {
                        heap.push({ dist: newDist, row: nextRow, col: nextCol });
                    }
                }
            }
        }
        return -1;
    }
}

module.exports = { Solution };
