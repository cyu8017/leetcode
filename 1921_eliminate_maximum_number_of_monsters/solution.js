// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

/**
 * @param {number[]} dist
 * @param {number[]} speed
 * @return {number}
 */
var eliminateMaximum = function(dist, speed) {
    const arrival = dist.map((d, i) => Math.ceil(d / speed[i])).sort((a, b) => a - b);
    for (let i = 0; i < arrival.length; i++) {
        if (arrival[i] <= i) return i;
    }
    return arrival.length;
};
