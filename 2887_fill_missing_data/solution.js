// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

/**
 * @param {object[]} products
 * @return {object[]}
 */
var fillMissingValues = function(products) {
    return products.map((r) => {
        if (Array.isArray(r)) {
            const q = r[1];
            return [r[0], q === null || q === undefined ? 0 : q, r[2]];
        }
        return { ...r, quantity: r.quantity == null ? 0 : r.quantity };
    });
};
