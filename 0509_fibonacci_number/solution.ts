// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

export class Solution {
    fib(n: number): number {
        if (n <= 1) return n;
        let previous = 0;
        let current = 1;
        for (let index = 2; index <= n; index += 1) {
            const next = previous + current;
            previous = current;
            current = next;
        }
        return current;
    }
}
