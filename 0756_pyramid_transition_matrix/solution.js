// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

/**
 * @param {string} bottom
 * @param {string[]} allowed
 * @return {boolean}
 */
var pyramidTransition = function(bottom, allowed) {
    const transitions = new Map();
    const memo = new Map();
    for (const triple of allowed) {
        const key = triple.substring(0, 2);
        if (!transitions.has(key)) transitions.set(key, []);
        transitions.get(key).push(triple[2]);
    }
    const build = (index, options, path) => {
        if (index === options.length) return dfs(path);
        for (const ch of options[index]) {
            if (build(index + 1, options, path + ch)) return true;
        }
        return false;
    };
    const dfs = (row) => {
        if (row.length === 1) return true;
        if (memo.has(row)) return memo.get(row);
        const options = [];
        for (let i = 0; i + 1 < row.length; i++) {
            const key = row.substring(i, i + 2);
            if (!transitions.has(key)) {
                memo.set(row, false);
                return false;
            }
            options.push(transitions.get(key));
        }
        const ok = build(0, options, '');
        memo.set(row, ok);
        return ok;
    };
    return dfs(bottom);
};
