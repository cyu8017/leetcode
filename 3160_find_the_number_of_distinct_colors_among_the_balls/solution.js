// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

/**
 * @param {number} limit
 * @param {number[][]} queries
 * @return {number[]}
 */
var queryResults = function(limit, queries) {
    const g = new Map();
    const cnt = new Map();
    const ans = new Array(queries.length);
    let ai = 0;
    for (const q of queries) {
        const x = q[0], y = q[1];
        cnt.set(y, (cnt.get(y) || 0) + 1);
        const old = g.get(x);
        if (old !== undefined) {
            const nv = cnt.get(old) - 1;
            if (nv === 0) cnt.delete(old);
            else cnt.set(old, nv);
        }
        g.set(x, y);
        ans[ai++] = cnt.size;
    }
    return ans;
};
