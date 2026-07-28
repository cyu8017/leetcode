// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

/**
 * @param {number[][]} workers
 * @param {number[][]} bikes
 * @return {number}
 */
var assignBikes = function(workers, bikes) {
    const m = bikes.length;
    const memo = new Map();

    function dp(i, mask) {
        if (i === workers.length) return 0;
        const key = i + "," + mask;
        if (memo.has(key)) return memo.get(key);
        let best = Infinity;
        const [wx, wy] = workers[i];
        for (let b = 0; b < m; b++) {
            if (mask & (1 << b)) continue;
            const [bx, by] = bikes[b];
            const dist = Math.abs(wx - bx) + Math.abs(wy - by);
            best = Math.min(best, dist + dp(i + 1, mask | (1 << b)));
        }
        memo.set(key, best);
        return best;
    }

    return dp(0, 0);
};
