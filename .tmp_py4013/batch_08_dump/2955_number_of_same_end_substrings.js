// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

var sameEndSubstringCount = function(s, queries) {
    const n = s.length;
    const pref = Array.from({length: n + 1}, () => new Array(26).fill(0));
    for (let i = 0; i < n; i++) {
        for (let c = 0; c < 26; c++) pref[i + 1][c] = pref[i][c];
        pref[i + 1][s.charCodeAt(i) - 97]++;
    }
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const l = queries[qi][0], r = queries[qi][1];
        let total = 0;
        for (let c = 0; c < 26; c++) {
            const cnt = pref[r + 1][c] - pref[l][c];
            total += cnt * (cnt + 1) / 2;
        }
        ans[qi] = total;
    }
    return ans;
};
