// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

export function maximumOddBinaryNumber(s: string): string {
    let ones = 0;
    for (const c of s) if (c === '1') ones++;
    const zeros = s.length - ones;
    return '1'.repeat(ones - 1) + '0'.repeat(zeros) + '1';
}
