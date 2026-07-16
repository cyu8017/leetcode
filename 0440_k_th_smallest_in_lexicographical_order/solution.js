// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution {
    findKthNumber(n, k) {
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

    _countSteps(n, first, last) {
        let steps = 0;
        while (first <= n) {
            steps += Math.min(n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }
}

module.exports = { Solution };
