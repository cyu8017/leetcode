// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var deleteGreatestValue = function(grid) {
    for (const row of grid) row.sort((a, b) => a - b);
    let ans = 0;
    const n = grid[0].length;
    for (let c = 0; c < n; c++) {
        let mx = 0;
        for (const row of grid) if (row[c] > mx) mx = row[c];
        ans += mx;
    }
    return ans;
};
