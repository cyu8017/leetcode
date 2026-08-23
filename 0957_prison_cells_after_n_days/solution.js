// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

/**
 * @param {number[]} cells
 * @param {number} n
 * @return {number[]}
 */
var prisonAfterNDays = function(cells, n) {
    const seen = new Map();
    let state = cells.slice();
    while (n > 0) {
        const key = state.join(",");
        if (seen.has(key)) {
            const cycle = seen.get(key) - n;
            n %= cycle;
            if (n === 0) break;
        }
        seen.set(key, n);
        const nxt = new Array(8).fill(0);
        for (let i = 1; i <= 6; i++) nxt[i] = state[i - 1] === state[i + 1] ? 1 : 0;
        state = nxt;
        n--;
    }
    return state;
};
