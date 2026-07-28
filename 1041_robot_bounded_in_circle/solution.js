// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

/**
 * @param {string} instructions
 * @return {boolean}
 */
var isRobotBounded = function(instructions) {
    let x = 0, y = 0, dx = 0, dy = 1;
    for (const ch of instructions) {
        if (ch === 'G') {
            x += dx;
            y += dy;
        } else if (ch === 'L') {
            [dx, dy] = [-dy, dx];
        } else {
            [dx, dy] = [dy, -dx];
        }
    }
    return (x === 0 && y === 0) || !(dx === 0 && dy === 1);
};
