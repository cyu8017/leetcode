// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
    const lose = new Map();
    const seen = new Set();
    for (const m of matches) {
        seen.add(m[0]);
        seen.add(m[1]);
        lose.set(m[1], (lose.get(m[1]) || 0) + 1);
    }
    const zero = [], one = [];
    for (const p of seen) {
        const L = lose.get(p) || 0;
        if (L === 0) zero.push(p);
        else if (L === 1) one.push(p);
    }
    zero.sort((a, b) => a - b);
    one.sort((a, b) => a - b);
    return [zero, one];
};
