// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

/**
 * @param {number} height
 * @param {number} width
 * @param {number[]} tree
 * @param {number[]} squirrel
 * @param {number[][]} nuts
 * @return {number}
 */
var minDistance = function(height, width, tree, squirrel, nuts) {
    const dist = (a, b) => Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    let total = 0;
    let bestSave = -Infinity;
    for (const nut of nuts) {
        const treeDist = dist(tree, nut);
        const squirrelDist = dist(squirrel, nut);
        total += 2 * treeDist;
        bestSave = Math.max(bestSave, treeDist - squirrelDist);
    }
    return total - bestSave;
};
