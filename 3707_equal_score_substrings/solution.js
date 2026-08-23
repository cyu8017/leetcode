// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

var scoreBalance = function(s) {
    let l = 0, r = 0;
    for (const c of s) r += (c.charCodeAt(0) - 97) + 1;
    for (let i = 0; i + 1 < s.length; i++) {
        const x = (s.charCodeAt(i) - 97) + 1;
        l += x;
        r -= x;
        if (l === r) return true;
    }
    return false;
};
