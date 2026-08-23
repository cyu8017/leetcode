// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

var winningPlayerCount = function(n, pick) {
    const cnt = Array.from({length: n}, () => new Array(11).fill(0));
    const s = new Set();
    for (const p of pick) {
        const x = p[0], y = p[1];
        cnt[x][y]++;
        if (cnt[x][y] > x) s.add(x);
    }
    return s.size;
};
