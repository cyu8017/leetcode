// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

var maximumScore = function(grid) {
    const n = grid.length;
    const prefix = Array.from({length: n}, () => new Array(n + 1).fill(0));
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < n; i++) prefix[j][i + 1] = prefix[j][i] + grid[i][j];
    }
    let prevPick = new Array(n + 1).fill(0), prevSkip = new Array(n + 1).fill(0);
    for (let j = 1; j < n; j++) {
        const currPick = new Array(n + 1).fill(0), currSkip = new Array(n + 1).fill(0);
        for (let curr = 0; curr <= n; curr++) {
            for (let prev = 0; prev <= n; prev++) {
                if (curr > prev) {
                    const score = prefix[j - 1][curr] - prefix[j - 1][prev];
                    currPick[curr] = Math.max(currPick[curr], prevSkip[prev] + score);
                    currSkip[curr] = Math.max(currSkip[curr], prevSkip[prev] + score);
                } else {
                    const score = prefix[j][prev] - prefix[j][curr];
                    currPick[curr] = Math.max(currPick[curr], prevPick[prev] + score);
                    currSkip[curr] = Math.max(currSkip[curr], prevPick[prev]);
                }
            }
        }
        prevPick = currPick;
        prevSkip = currSkip;
    }
    let ans = -Infinity;
    for (const v of prevPick) ans = Math.max(ans, v);
    return ans;
};
