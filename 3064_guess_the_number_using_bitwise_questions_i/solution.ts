// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

export function findNumber(): number {
    let n = 0;
    for (let i = 0; i < 32; i++)
        if (commonSetBits(1 << i) > 0) n |= 1 << i;
    return n;
}
