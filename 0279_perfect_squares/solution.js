// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    const squares = [];
    for (let value = 1; value * value <= n; value++) {
        squares.push(value * value);
    }

    const queue = [[n, 0]];
    const visited = new Set([n]);

    while (queue.length > 0) {
        const [remain, steps] = queue.shift();
        if (remain === 0) {
            return steps;
        }
        for (const square of squares) {
            const next = remain - square;
            if (next < 0) {
                break;
            }
            if (!visited.has(next)) {
                visited.add(next);
                queue.push([next, steps + 1]);
            }
        }
    }
    return 0;
};
