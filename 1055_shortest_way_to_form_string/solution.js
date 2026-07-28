// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

/**
 * @param {string} source
 * @param {string} target
 * @return {number}
 */
var shortestWay = function(source, target) {
    const sourceSet = new Set(source);
    for (const ch of target) {
        if (!sourceSet.has(ch)) return -1;
    }
    let ans = 0;
    let i = 0;
    const n = target.length;
    while (i < n) {
        ans++;
        for (const ch of source) {
            if (i < n && target[i] === ch) i++;
        }
    }
    return ans;
};
