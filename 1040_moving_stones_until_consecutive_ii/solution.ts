// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

function numMovesStonesII(stones: number[]): number[] {
    stones.sort((a, b) => a - b);
    const n = stones.length;
    const maxMoves = Math.max(
        stones[n - 1] - stones[1] - n + 2,
        stones[n - 2] - stones[0] - n + 2,
    );
    let minMoves = maxMoves;
    let i = 0;
    for (let j = 0; j < n; j++) {
        while (stones[j] - stones[i] + 1 > n) i++;
        const inside = j - i + 1;
        if (inside === n - 1 && stones[j] - stones[i] + 1 === n - 1) {
            minMoves = Math.min(minMoves, 2);
        } else {
            minMoves = Math.min(minMoves, n - inside);
        }
    }
    return [minMoves, maxMoves];
}
