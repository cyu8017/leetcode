// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

function minCostToMoveChips(position: number[]): number {
    const odd = position.filter((x) => x & 1).length;
    return Math.min(odd, position.length - odd);
}
