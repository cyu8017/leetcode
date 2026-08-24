// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

export function circularGameLosers(n: any, k: any): any {
    const seen = new Array(n + 1).fill(false);
    let cur = 1, step = 1;
    while (!seen[cur]) {
        seen[cur] = true;
        cur = (cur - 1 + step * k) % n + 1;
        step++;
    }
    const ans = [];
    for (let i = 1; i <= n; i++) if (!seen[i]) ans.push(i);
    return ans;
}
