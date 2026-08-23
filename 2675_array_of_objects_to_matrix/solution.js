// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

var jsonToMatrix = function(arr) {
    const isObj = (x) => x !== null && typeof x === "object" && !Array.isArray(x);
    const flatten = (obj, prefix, out) => {
        if (!isObj(obj) && !Array.isArray(obj)) {
            out[prefix] = obj;
            return;
        }
        if (Array.isArray(obj)) {
            if (!obj.length) return;
            for (let i = 0; i < obj.length; i++)
                flatten(obj[i], prefix ? prefix + "." + i : String(i), out);
            return;
        }
        const keys = Object.keys(obj);
        if (!keys.length) return;
        for (const k of keys)
            flatten(obj[k], prefix ? prefix + "." + k : k, out);
    };
    const maps = arr.map((o) => {
        const m = {};
        flatten(o, "", m);
        return m;
    });
    const keySet = new Set();
    for (const m of maps) for (const k of Object.keys(m)) keySet.add(k);
    const keys = [...keySet].sort();
    const mat = [keys];
    for (const m of maps) mat.push(keys.map((k) => (k in m ? m[k] : "")));
    return mat;
};
