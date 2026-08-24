// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

export function maxNumber(n: number): number {
    let len = 0;
    let x = BigInt(n);
    while (x > 0n) { len++; x >>= 1n; }
    return Number((1n << BigInt(len - 1)) - 1n);
}
