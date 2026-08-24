// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

/**
 * @param {object[]} report
 * @return {object[]}
 */
var meltTable = function(report) {
    const out = [];
    for (const r of report) {
        if (Array.isArray(r)) {
            const product = r[0];
            for (let q = 1; q <= 4; q++) out.push({ product, quarter: 'quarter_' + q, sales: r[q] });
        } else {
            for (const q of ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4']) {
                out.push({ product: r.product, quarter: q, sales: r[q] });
            }
        }
    }
    return out;
};
