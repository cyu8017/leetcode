// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

export function minDistance(height: number, width: number, tree: number[], squirrel: number[], nuts: number[][]): number {
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
}
