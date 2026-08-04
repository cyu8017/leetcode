// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    const m = maze.length, n = maze[0].length;
    const [er, ec] = entrance;
    const q = [[er, ec, 0]];
    maze[er][ec] = "+";
    for (let qi = 0; qi < q.length; qi++) {
        const [r, c, d] = q[qi];
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] === ".") {
                if (nr === 0 || nr === m - 1 || nc === 0 || nc === n - 1) return d + 1;
                maze[nr][nc] = "+";
                q.push([nr, nc, d + 1]);
            }
        }
    }
    return -1;
};
