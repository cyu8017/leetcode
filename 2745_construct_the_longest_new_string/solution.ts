// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

export function longestString(x: number, y: number, z: number): number {
    if (x < y) return (2 * x + 1 + z) * 2;
    if (y < x) return (2 * y + 1 + z) * 2;
    return (x + y + z) * 2;
}
