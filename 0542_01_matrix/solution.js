// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

class Solution {
    updateMatrix(mat) {
        const rows = mat.length;
        const cols = mat[0].length;
        const dist = Array.from({ length: rows }, () => Array(cols).fill(1e9));
        const queue = [];

        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                if (mat[row][col] === 0) {
                    dist[row][col] = 0;
                    queue.push([row, col]);
                }
            }
        }

        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (queue.length) {
            const [row, col] = queue.shift();
            for (const [dr, dc] of directions) {
                const nr = row + dr;
                const nc = col + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && dist[nr][nc] > dist[row][col] + 1) {
                    dist[nr][nc] = dist[row][col] + 1;
                    queue.push([nr, nc]);
                }
            }
        }

        return dist;
    }
}

module.exports = { Solution };
