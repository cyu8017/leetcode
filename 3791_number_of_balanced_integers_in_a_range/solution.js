// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number_of_balanced_integers_in_a_range/

var countBalanced = function(low, high) {
    const BASE = 90;
    let num = '';
    let f = Array.from({length: 20}, () => new Array(181).fill(-1));
    const dfs = (pos, diff, lim) => {
        if (pos >= num.length) return diff === 0 ? 1 : 0;
        if (!lim && f[pos][diff + BASE] !== -1) return f[pos][diff + BASE];
        const up = lim ? num.charCodeAt(pos) - 48 : 9;
        let res = 0;
        for (let i = 0; i <= up; i++) {
            if (pos % 2 === 0) res += dfs(pos + 1, diff + i, lim && i === up);
            else res += dfs(pos + 1, diff - i, lim && i === up);
        }
        if (!lim) f[pos][diff + BASE] = res;
        return res;
    };
    if (high < 11) return 0;
    if (low < 11) low = 11;
    num = String(low - 1);
    f = Array.from({length: 20}, () => new Array(181).fill(-1));
    const a = dfs(0, 0, true);
    num = String(high);
    f = Array.from({length: 20}, () => new Array(181).fill(-1));
    const b = dfs(0, 0, true);
    return b - a;
};
