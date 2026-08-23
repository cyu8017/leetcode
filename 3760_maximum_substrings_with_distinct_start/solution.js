// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

var maxDistinct = function(s) {
    const cnt = new Array(26).fill(0);
    let ans = 0;
    for (const c of s) {
        const i = c.charCodeAt(0) - 97;
        cnt[i]++;
        if (cnt[i] === 1) ans++;
    }
    return ans;
};
