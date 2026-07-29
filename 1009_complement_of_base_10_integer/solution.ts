// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

function bitwiseComplement(n: number): number {
    if (n === 0) return 1;
    let mask = 1;
    while (mask <= n) mask <<= 1;
    return n ^ (mask - 1);
}
