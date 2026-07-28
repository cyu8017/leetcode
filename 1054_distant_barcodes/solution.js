// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

/**
 * @param {number[]} barcodes
 * @return {number[]}
 */
var rearrangeBarcodes = function(barcodes) {
    const count = new Map();
    for (const x of barcodes) count.set(x, (count.get(x) || 0) + 1);
    const items = [...count.entries()].sort((a, b) => b[1] - a[1]);
    const n = barcodes.length;
    const ans = new Array(n);
    let i = 0;
    for (const [value, freq] of items) {
        for (let k = 0; k < freq; k++) {
            ans[i] = value;
            i += 2;
            if (i >= n) i = 1;
        }
    }
    return ans;
};
