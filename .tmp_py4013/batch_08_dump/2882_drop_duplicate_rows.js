// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

/**
 * @param {object[]} customers
 * @return {object[]}
 */
var dropDuplicateEmails = function(customers) {
    const seen = new Set();
    const out = [];
    for (const r of customers) {
        const email = Array.isArray(r) ? r[2] : r.email;
        if (seen.has(email)) continue;
        seen.add(email);
        out.push(r);
    }
    return out;
};
