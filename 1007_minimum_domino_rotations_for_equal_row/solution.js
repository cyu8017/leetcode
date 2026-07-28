// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

/**
 * @param {number[]} tops
 * @param {number[]} bottoms
 * @return {number}
 */
var minDominoRotations = function(tops, bottoms) {
    const check = (target) => {
        let rotTop = 0, rotBot = 0;
        for (let i = 0; i < tops.length; i++) {
            if (tops[i] !== target && bottoms[i] !== target) return Infinity;
            if (tops[i] !== target) rotTop++;
            if (bottoms[i] !== target) rotBot++;
        }
        return Math.min(rotTop, rotBot);
    };
    const ans = Math.min(check(tops[0]), check(bottoms[0]));
    return ans === Infinity ? -1 : ans;
};
