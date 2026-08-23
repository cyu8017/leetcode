// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

/**
 * @param {any} obj
 * @param {Function} fn
 * @return {any}
 */
var deepFilter = function(obj, fn) {
    if (typeof obj !== 'object' || obj === null) {
        return fn(obj) ? obj : undefined;
    }
    if (Array.isArray(obj)) {
        const res = [];
        for (const v of obj) {
            const f = deepFilter(v, fn);
            if (f !== undefined) res.push(f);
        }
        return res.length ? res : undefined;
    }
    const res = {};
    for (const k of Object.keys(obj)) {
        const f = deepFilter(obj[k], fn);
        if (f !== undefined) res[k] = f;
    }
    return Object.keys(res).length ? res : undefined;
};
