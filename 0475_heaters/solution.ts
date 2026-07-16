// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

export class Solution {
    findRadius(houses: number[], heaters: number[]): number {
        const sortedHeaters = [...heaters].sort((a, b) => a - b);
        let radius = 0;

        for (const house of houses) {
            let position = 0;
            while (position < sortedHeaters.length && sortedHeaters[position] < house) {
                position += 1;
            }
            const distances: number[] = [];
            if (position < sortedHeaters.length) {
                distances.push(Math.abs(sortedHeaters[position] - house));
            }
            if (position > 0) {
                distances.push(Math.abs(sortedHeaters[position - 1] - house));
            }
            radius = Math.max(radius, Math.min(...distances));
        }
        return radius;
    }
}
