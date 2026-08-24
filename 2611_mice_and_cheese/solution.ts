// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

export function miceAndCheese(reward1: number[], reward2: number[], k: number): number {
    const n = reward1.length;
    const diff = new Array(n);
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        ans += reward2[i];
        diff[i] = reward1[i] - reward2[i];
    }
    diff.sort((a, b) => b - a);
    for (let i = 0; i < k; ++i) ans += diff[i];
    return ans;
}
