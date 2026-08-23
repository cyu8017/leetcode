// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

var maxActiveSectionsAfterTrade = function(s, queries) {
    let ones = 0;
    for (const c of s) if (c === "1") ones++;
    const ans = new Array(queries.length);
    for (let i = 0; i < ans.length; i++) ans[i] = ones;
    return ans;
};
