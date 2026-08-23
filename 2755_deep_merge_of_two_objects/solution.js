// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

/**
 * @param {any} obj1
 * @param {any} obj2
 * @return {any}
 */
var deepMerge = function(obj1, obj2) {
    const isObj = (x) => x !== null && typeof x === 'object' && !Array.isArray(x);
    const isArr = Array.isArray;
    if (isObj(obj1) && isObj(obj2)) {
        const res = {...obj1};
        for (const k of Object.keys(obj2)) {
            if (k in res) res[k] = deepMerge(res[k], obj2[k]);
            else res[k] = obj2[k];
        }
        return res;
    }
    if (isArr(obj1) && isArr(obj2)) {
        const n = Math.max(obj1.length, obj2.length);
        const res = new Array(n);
        for (let i = 0; i < n; i++) {
            if (i >= obj1.length) res[i] = obj2[i];
            else if (i >= obj2.length) res[i] = obj1[i];
            else res[i] = deepMerge(obj1[i], obj2[i]);
        }
        return res;
    }
    return obj2;
};
