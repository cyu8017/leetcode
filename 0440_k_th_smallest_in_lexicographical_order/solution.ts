// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

export class Solution {
    findKthNumber(n: number, k: number): number {
        let current = 1;
        k -= 1;

        while (k > 0) {
            const steps = this._countSteps(n, current, current + 1);
            if (steps <= k) {
                current += 1;
                k -= steps;
            } else {
                current *= 10;
                k -= 1;
            }
        }

        return current;
    }

    private _countSteps(n: number, first: number, last: number): number {
        let steps = 0;
        while (first <= n) {
            steps += Math.min(n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }
}
