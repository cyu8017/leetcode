// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
    let row = [poured];
    for (let r = 0; r < query_row; r++) {
        const nextRow = new Array(r + 2).fill(0);
        for (let i = 0; i < row.length; i++) {
            const overflow = (row[i] - 1.0) / 2.0;
            if (overflow > 0) {
                nextRow[i] += overflow;
                nextRow[i + 1] += overflow;
            }
        }
        row = nextRow;
    }
    return Math.min(1.0, row[query_glass]);
};
