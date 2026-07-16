// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

export class Solution {
    numberOfBoomerangs(points: number[][]): number {
        let total = 0;
        for (const anchor of points) {
            const distances = new Map<number, number>();
            for (const other of points) {
                const dx = anchor[0] - other[0];
                const dy = anchor[1] - other[1];
                const distance = dx * dx + dy * dy;
                distances.set(distance, (distances.get(distance) ?? 0) + 1);
            }
            for (const count of distances.values()) {
                total += count * (count - 1);
            }
        }
        return total;
    }
}
