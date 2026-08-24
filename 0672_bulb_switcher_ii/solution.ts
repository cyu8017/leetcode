// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

export function flipLights(n: number, presses: number): number {
    n = Math.min(n, 3);
    if (presses === 0) return 1;
    const onePress = [2, 3, 4];
    const twoPress = [2, 4, 7];
    const manyPress = [2, 4, 8];
    if (presses === 1) return onePress[n - 1];
    if (presses === 2) return twoPress[n - 1];
    return manyPress[n - 1];
}
