// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

/**
 * @param {number[]} forbidden
 * @param {number} a
 * @param {number} b
 * @param {number} x
 * @return {number}
 */
var minimumJumps = function(forbidden, a, b, x) {
    const bad = new Set(forbidden);
    const limit = Math.max(x, ...forbidden) + a + b;
    const q = [[0, 0, false]];
    const seen = new Set(["0,0"]);
    while (q.length) {
        const [p, d, back] = q.shift();
        if (p === x) return d;
        for (const [np, nb] of [[p + a, false], [p - b, true]]) {
            const key = `${np},${nb ? 1 : 0}`;
            if (np >= 0 && np <= limit && !bad.has(np) && !seen.has(key) && !(back && nb)) {
                seen.add(key);
                q.push([np, d + 1, nb]);
            }
        }
    }
    return -1;
};
