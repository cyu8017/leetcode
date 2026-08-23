// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

/**
 * @param {number[]} commands
 * @param {number[][]} obstacles
 * @return {number}
 */
var robotSim = function(commands, obstacles) {
    const encode = (x, y) => ((x + 30000) << 20) | (y + 30000);
    const blocked = new Set();
    for (const [ox, oy] of obstacles) blocked.add(encode(ox, oy));
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let x = 0, y = 0, d = 0, best = 0;
    for (const cmd of commands) {
        if (cmd === -1) d = (d + 1) % 4;
        else if (cmd === -2) d = (d + 3) % 4;
        else {
            const [dx, dy] = dirs[d];
            for (let step = 0; step < cmd; step++) {
                const nx = x + dx, ny = y + dy;
                if (blocked.has(encode(nx, ny))) break;
                x = nx;
                y = ny;
            }
            best = Math.max(best, x * x + y * y);
        }
    }
    return best;
};
