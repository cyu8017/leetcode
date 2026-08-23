// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        const out = [];
        for (const x of obj) {
            const v = compactObject(x);
            if (v) out.push(v);
        }
        return out;
    }
    if (obj !== null && typeof obj === "object") {
        const out = {};
        for (const k of Object.keys(obj)) {
            const v = compactObject(obj[k]);
            if (v) out[k] = v;
        }
        return out;
    }
    return obj;
};
