// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

/**
 * @param {number[][]} rooms
 * @return {void}
 */
var wallsAndGates = function(rooms) {
    if (!rooms.length) {
        return;
    }
    const rows = rooms.length;
    const cols = rooms[0].length;
    const queue = [];
    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            if (rooms[row][col] === 0) {
                queue.push([row, col]);
            }
        }
    }
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (queue.length > 0) {
        const [row, col] = queue.shift();
        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && rooms[nr][nc] === 2147483647) {
                rooms[nr][nc] = rooms[row][col] + 1;
                queue.push([nr, nc]);
            }
        }
    }
};
