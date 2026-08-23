// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

class Solution {
    fib(n) {
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

module.exports = { Solution };
