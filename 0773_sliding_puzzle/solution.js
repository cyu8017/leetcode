// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

/**
 * @param {number[][]} board
 * @return {number}
 */
var slidingPuzzle = function(board) {
    let start = '';
    for (const row of board) for (const cell of row) start += cell;
    const target = '123450';
    const neighbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]];
    const q = [start];
    const stepsQ = [0];
    const seen = new Set([start]);
    while (q.length > 0) {
        const state = q.shift();
        const steps = stepsQ.shift();
        if (state === target) return steps;
        const zero = state.indexOf('0');
        for (const nei of neighbors[zero]) {
            const nxt = state.split('');
            const tmp = nxt[zero];
            nxt[zero] = nxt[nei];
            nxt[nei] = tmp;
            const ns = nxt.join('');
            if (!seen.has(ns)) {
                seen.add(ns);
                q.push(ns);
                stepsQ.push(steps + 1);
            }
        }
    }
    return -1;
};
