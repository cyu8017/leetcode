// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

var areDeeplyEqual = function(o1, o2) {
    if (o1 === o2) return true;
    if (typeof o1 !== typeof o2) return false;
    if (o1 === null || o2 === null) return false;
    if (typeof o1 !== "object") return false;
    const a1 = Array.isArray(o1), a2 = Array.isArray(o2);
    if (a1 !== a2) return false;
    if (a1) {
        if (o1.length !== o2.length) return false;
        for (let i = 0; i < o1.length; i++) if (!areDeeplyEqual(o1[i], o2[i])) return false;
        return true;
    }
    const k1 = Object.keys(o1), k2 = Object.keys(o2);
    if (k1.length !== k2.length) return false;
    for (const k of k1) if (!areDeeplyEqual(o1[k], o2[k])) return false;
    return true;
};
