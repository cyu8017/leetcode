// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

export class Solution {
    findCircleNum(isConnected: number[][]): number {
        const n = isConnected.length;
        const parent = Array.from({ length: n }, (_, i) => i);

        const find = (x: number): number => {
            while (parent[x] !== x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };

        const union = (a: number, b: number): void => {
            const ra = find(a);
            const rb = find(b);
            if (ra !== rb) parent[rb] = ra;
        };

        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (isConnected[i][j]) union(i, j);
            }
        }

        return parent.reduce((count, _, i) => count + (find(i) === i ? 1 : 0), 0);
    }
}
