// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

var longestCommonPrefix = function(s, t) {
    let i = 0, j = 0;
    let removed = false;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) {
            i++;
            j++;
            continue;
        }
        if (removed) break;
        removed = true;
        i++;
    }
    return j;
};
