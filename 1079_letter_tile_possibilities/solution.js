// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

/**
 * @param {string} tiles
 * @return {number}
 */
var numTilePossibilities = function(tiles) {
    const count = new Map();
    for (const ch of tiles) count.set(ch, (count.get(ch) || 0) + 1);

    function dfs() {
        let total = 0;
        for (const [ch, freq] of count) {
            if (freq === 0) continue;
            count.set(ch, freq - 1);
            total += 1 + dfs();
            count.set(ch, freq);
        }
        return total;
    }

    return dfs();
};
