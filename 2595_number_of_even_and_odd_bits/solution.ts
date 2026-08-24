// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

export function evenOddBit(n: number): number[] {
    let even = 0, odd = 0;
    for (let i = 0; n > 0; ++i, n >>= 1) {
        if ((n & 1) !== 0) {
            if (i % 2 === 0) even++;
            else odd++;
        }
    }
    return [even, odd];
}
