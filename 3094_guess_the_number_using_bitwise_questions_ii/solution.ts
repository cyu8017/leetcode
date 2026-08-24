// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

export function findNumber(): number {
    let n = 0;
    for (let i = 0; i < 32; i++) {
        const count1 = commonBits(1 << i);
        const count2 = commonBits(1 << i);
        if (count1 > count2) n |= 1 << i;
    }
    return n;
}
