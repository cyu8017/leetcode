// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

export function maximumXOR(nums: number[]): number {
    let ans = 0;
    for (const x of nums) ans |= x;
    return ans;
}
