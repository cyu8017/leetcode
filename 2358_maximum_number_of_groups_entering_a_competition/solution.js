// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

/**
 * @param {number[]} grades
 * @return {number}
 */
var maximumGroups = function(grades) {
    const n = grades.length;
    let k = 0;
    while ((k + 1) * (k + 2) / 2 <= n) k++;
    return k;
};
