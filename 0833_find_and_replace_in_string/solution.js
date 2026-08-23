// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

/**
 * @param {string} s
 * @param {number[]} indices
 * @param {string[]} sources
 * @param {string[]} targets
 * @return {string}
 */
var findReplaceString = function(s, indices, sources, targets) {
    const replaceLen = new Map();
    const replaceStr = new Map();
    for (let k = 0; k < indices.length; k++) {
        const i = indices[k];
        if (s.startsWith(sources[k], i)) {
            replaceLen.set(i, sources[k].length);
            replaceStr.set(i, targets[k]);
        }
    }
    let out = "";
    let i = 0;
    const n = s.length;
    while (i < n) {
        if (replaceStr.has(i)) {
            out += replaceStr.get(i);
            i += replaceLen.get(i);
        } else {
            out += s[i];
            i++;
        }
    }
    return out;
};
