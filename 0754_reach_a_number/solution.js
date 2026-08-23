// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

/**
 * @param {number} target
 * @return {number}
 */
var reachNumber = function(target) {
    target = Math.abs(target);
    let steps = 0, total = 0;
    while (total < target || (total - target) % 2 !== 0) {
        steps++;
        total += steps;
    }
    return steps;
};
