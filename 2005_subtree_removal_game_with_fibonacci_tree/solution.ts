// LeetCode 2005 - Subtree Removal Game with Fibonacci Tree
// https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/

export function findGameWinner(n: number): boolean {
    return n % 6 !== 1;
}
