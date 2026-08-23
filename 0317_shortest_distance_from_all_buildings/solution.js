// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestDistance = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const buildings = grid.flat().filter((cell) => cell === 1).length;
    const distances = Array.from({ length: rows }, () => Array(cols).fill(0));
    const reach = Array.from({ length: rows }, () => Array(cols).fill(0));
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            if (grid[row][col] !== 1) {
                continue;
            }
            const queue = [[row, col, 0]];
            const visited = new Set([`${row},${col}`]);
            while (queue.length > 0) {
                const [currentRow, currentCol, distance] = queue.shift();
                for (const [dr, dc] of directions) {
                    const nr = currentRow + dr;
                    const nc = currentCol + dc;
                    const key = `${nr},${nc}`;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] === 0 && !visited.has(key)) {
                        visited.add(key);
                        distances[nr][nc] += distance + 1;
                        reach[nr][nc] += 1;
                        queue.push([nr, nc, distance + 1]);
                    }
                }
            }
        }
    }

    let best = Infinity;
    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            if (grid[row][col] === 0 && reach[row][col] === buildings) {
                best = Math.min(best, distances[row][col]);
            }
        }
    }
    return best === Infinity ? -1 : best;
};
