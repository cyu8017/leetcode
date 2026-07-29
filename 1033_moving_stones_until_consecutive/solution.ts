// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

function numMovesStones(a: number, b: number, c: number): number[] {
    const [x, y, z] = [a, b, c].sort((p, q) => p - q);
    let minMoves;
    if (z - x === 2) minMoves = 0;
    else if (y - x <= 2 || z - y <= 2) minMoves = 1;
    else minMoves = 2;
    return [minMoves, z - x - 2];
}
