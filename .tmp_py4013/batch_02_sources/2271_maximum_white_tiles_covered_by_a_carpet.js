// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

/**
 * @param {number[][]} tiles
 * @param {number} carpetLen
 * @return {number}
 */
var maximumWhiteTiles = function(tiles, carpetLen) {
    tiles.sort((a, b) => a[0] - b[0]);
    const n = tiles.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1);
    let ans = 0, j = 0;
    for (let i = 0; i < n; i++) {
        const end = tiles[i][0] + carpetLen - 1;
        while (j < n && tiles[j][0] <= end) j++;
        let cover = pref[j] - pref[i];
        if (j > 0 && tiles[j - 1][1] > end) cover -= tiles[j - 1][1] - end;
        ans = Math.max(ans, cover);
    }
    return ans;
};
