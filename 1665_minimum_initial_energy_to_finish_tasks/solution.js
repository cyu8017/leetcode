// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

/**
 * @param {number[][]} tasks
 * @return {number}
 */
var minimumEffort = function(tasks) {
    tasks.sort((a, b) => (b[1] - b[0]) - (a[1] - a[0]));
    let energy = 0, spent = 0;
    for (const [cost, minimum] of tasks) {
        energy = Math.max(energy, spent + minimum);
        spent += cost;
    }
    return energy;
};
