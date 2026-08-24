// LeetCode 3596 - Minimum Cost Path with Alternating Directions I
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/

export function minCost(m: any, n: any): any {
    if (m === 1 && n === 1) return 1;
    if (m === 1 && n === 2) return 3;
    if (m === 2 && n === 1) return 3;
    return -1;
}
