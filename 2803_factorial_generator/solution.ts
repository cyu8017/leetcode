// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

export function* factorialGenerator(n: number): Generator<number> {
    let cur = 1;
    for (let i = 1; i <= n; i++) {
        cur *= i;
        yield cur;
    }
}
