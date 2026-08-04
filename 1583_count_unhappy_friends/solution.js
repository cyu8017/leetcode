// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

/**
 * @param {number} n
 * @param {number[][]} preferences
 * @param {number[][]} pairs
 * @return {number}
 */
var unhappyFriends = function(n, preferences, pairs) {
    const rank = preferences.map((pref) => {
        const map = {};
        pref.forEach((friend, i) => { map[friend] = i; });
        return map;
    });
    const partner = {};
    for (const [a, b] of pairs) {
        partner[a] = b;
        partner[b] = a;
    }
    let unhappy = 0;
    for (let x = 0; x < n; x++) {
        const y = partner[x];
        const better = preferences[x].slice(0, rank[x][y]);
        if (better.some((u) => rank[u][x] < rank[u][partner[u]])) unhappy++;
    }
    return unhappy;
};
