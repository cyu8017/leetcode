// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

export function flowerGame(n: any, m: any): any {
    const a1 = ((n + 1) / 2) | 0, b1 = ((m + 1) / 2) | 0;
    const a2 = (n / 2) | 0, b2 = (m / 2) | 0;
    return a1 * b2 + a2 * b1;
}
