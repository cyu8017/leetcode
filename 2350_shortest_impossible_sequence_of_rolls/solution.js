// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

/**
 * @param {number[]} rolls
 * @param {number} k
 * @return {number}
 */
var shortestSequence = function(rolls, k) {
    const seen = new Set();
    let ans = 1;
    for (const r of rolls) {
        seen.add(r);
        if (seen.size === k) {
            ans++;
            seen.clear();
        }
    }
    return ans;
};
