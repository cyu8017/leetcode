// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

export function grayCode(n: number): number[] {
    const result: number[] = [];
    const size = 1 << n;
    for (let i = 0; i < size; i++) {
        result.push(i ^ (i >> 1));
    }
    return result;
}
