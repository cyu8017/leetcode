// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

export function findWinningPlayer(skills: any, k: any): any {
    const n = skills.length;
    k = Math.min(k, n - 1);
    let i = 0, cnt = 0;
    for (let j = 1; j < n; j++) {
        if (skills[i] < skills[j]) { i = j; cnt = 1; }
        else cnt++;
        if (cnt === k) break;
    }
    return i;
}
