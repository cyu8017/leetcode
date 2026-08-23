// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

Array.prototype.groupBy = function(fn) {
    const out = {};
    for (const x of this) {
        const k = fn(x);
        if (!out[k]) out[k] = [];
        out[k].push(x);
    }
    return out;
};
