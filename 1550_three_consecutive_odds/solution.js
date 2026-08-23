// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    let run = 0;
    for (const value of arr) {
        run = value & 1 ? run + 1 : 0;
        if (run === 3) return true;
    }
    return false;
};
