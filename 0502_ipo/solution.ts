// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

export class Solution {
    findMaximizedCapital(k: number, w: number, profits: number[], capital: number[]): number {
        const projects = capital.map((cap, index) => [cap, profits[index]] as [number, number]).sort((a, b) => a[0] - b[0]);
        const available: number[] = [];
        let index = 0;
        for (let round = 0; round < k; round += 1) {
            while (index < projects.length && projects[index][0] <= w) {
                available.push(-projects[index][1]);
                available.sort((a, b) => a - b);
                index += 1;
            }
            if (!available.length) break;
            w -= available.shift() as number;
        }
        return w;
    }
}
