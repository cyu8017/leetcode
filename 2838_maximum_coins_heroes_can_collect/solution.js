// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

/**
 * @param {number[]} heroes
 * @param {number[]} monsters
 * @param {number[]} coins
 * @return {number[]}
 */
var maximumCoins = function(heroes, monsters, coins) {
    const n = monsters.length;
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => monsters[a] - monsters[b]);
    const pref = Array(n + 1).fill(0);
    const ms = Array(n);
    for (let i = 0; i < n; i++) {
        ms[i] = monsters[idx[i]];
        pref[i + 1] = pref[i] + coins[idx[i]];
    }
    const upperBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >>> 1;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    return heroes.map((h) => pref[upperBound(ms, h)]);
};
