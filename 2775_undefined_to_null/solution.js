// LeetCode 2775 - Undefined to Null
// https://leetcode.com/problems/undefined-to-null/

/**
 * @param {any} obj
 * @return {any}
 */
var undefinedToNull = function(obj) {
    if (obj === undefined) return null;
    if (obj === null || typeof obj !== 'object') return obj;
    if (Array.isArray(obj)) {
        for (let i = 0; i < obj.length; i++) obj[i] = undefinedToNull(obj[i]);
        return obj;
    }
    for (const k of Object.keys(obj)) obj[k] = undefinedToNull(obj[k]);
    return obj;
};
