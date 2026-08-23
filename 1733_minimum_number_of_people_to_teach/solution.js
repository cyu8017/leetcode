// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

/**
 * @param {number} n
 * @param {number[][]} languages
 * @param {number[][]} friendships
 * @return {number}
 */
var minimumTeachings = function(n, languages, friendships) {
    const known = languages.map((items) => new Set(items));
    const need = new Set();
    for (const [u, v] of friendships) {
        let shares = false;
        for (const lang of known[u - 1]) {
            if (known[v - 1].has(lang)) {
                shares = true;
                break;
            }
        }
        if (!shares) {
            need.add(u - 1);
            need.add(v - 1);
        }
    }
    if (need.size === 0) {
        return 0;
    }
    let best = Infinity;
    for (let lang = 1; lang <= n; lang++) {
        let teach = 0;
        for (const user of need) {
            if (!known[user].has(lang)) teach++;
        }
        best = Math.min(best, teach);
    }
    return best;
};
