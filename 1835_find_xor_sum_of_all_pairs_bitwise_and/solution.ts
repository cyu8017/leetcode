// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

function getXORSum(arr1: number[], arr2: number[]): number {
    let xor1 = 0, xor2 = 0;
    for (const x of arr1) xor1 ^= x;
    for (const x of arr2) xor2 ^= x;
    return xor1 & xor2;
}
