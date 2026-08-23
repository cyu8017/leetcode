// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

/**
 * @param {string[]} strs
 * @return {number}
 */
var numSimilarGroups = function(strs) {
    const n = strs.length;
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const similar = (a, b) => {
        let d0 = -1, d1 = -1, diffs = 0;
        for (let i = 0; i < a.length; i++) {
            if (a[i] !== b[i]) {
                diffs++;
                if (diffs > 2) return false;
                if (d0 < 0) d0 = i;
                else d1 = i;
            }
        }
        return diffs === 0 || (diffs === 2 && a[d0] === b[d1] && a[d1] === b[d0]);
    };
    let groups = n;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (similar(strs[i], strs[j])) {
                const pi = find(i), pj = find(j);
                if (pi !== pj) {
                    parent[pi] = pj;
                    groups--;
                }
            }
        }
    }
    return groups;
};
