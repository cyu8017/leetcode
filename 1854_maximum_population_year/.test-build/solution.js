"use strict";
// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/
function maximumPopulation(logs) {
    const diff = new Array(101).fill(0);
    for (const [birth, death] of logs) {
        diff[birth - 1950]++;
        diff[death - 1950]--;
    }
    let bestYear = 1950, bestPop = 0, pop = 0;
    for (let offset = 0; offset < 101; offset++) {
        pop += diff[offset];
        if (pop > bestPop) {
            bestPop = pop;
            bestYear = 1950 + offset;
        }
    }
    return bestYear;
}
