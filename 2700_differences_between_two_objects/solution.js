// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

var objDiff = function(obj1, obj2) {
    const diff = {};
    for (const k of Object.keys(obj1)) {
        if (!(k in obj2)) continue;
        const v1 = obj1[k], v2 = obj2[k];
        if (typeof v1 === "object" && v1 && typeof v2 === "object" && v2 && !Array.isArray(v1) && !Array.isArray(v2)) {
            const child = objDiff(v1, v2);
            if (Object.keys(child).length) diff[k] = child;
        } else if (Array.isArray(v1) && Array.isArray(v2)) {
            const child = objDiff(v1, v2);
            if (Object.keys(child).length) diff[k] = child;
        } else if (v1 !== v2) {
            diff[k] = [v1, v2];
        }
    }
    return diff;
};
