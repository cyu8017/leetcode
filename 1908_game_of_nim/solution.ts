// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

function nimGame(piles: number[]): boolean {
    let x = 0;
    for (const p of piles) x ^= p;
    return x !== 0;
}
