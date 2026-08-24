// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

export function findIntegers(n: number): number {
    const fib = Array(32).fill(0);
    fib[0] = 1;
    fib[1] = 2;
    for (let i = 2; i < 32; ++i) fib[i] = fib[i - 1] + fib[i - 2];
    let answer = 0;
    let prevBit = 0;
    for (let bit = 30; bit >= 0; --bit) {
        if ((n & (1 << bit)) !== 0) {
            answer += fib[bit];
            if (prevBit === 1) return answer;
            prevBit = 1;
        } else {
            prevBit = 0;
        }
    }
    return answer + 1;
}
