// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

export function superEggDrop(k: number, n: number): number {
    const dp = new Array(k + 1).fill(0);
    let moves = 0;
    while (dp[k] < n) {
        moves++;
        for (let eggs = k; eggs >= 1; eggs--) {
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
        }
    }
    return moves;
}
