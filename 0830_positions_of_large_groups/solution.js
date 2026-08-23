// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

/**
 * @param {string} s
 * @return {number[][]}
 */
var largeGroupPositions = function(s) {
    const ans = [];
    const n = s.length;
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        if (j - i >= 3) ans.push([i, j - 1]);
        i = j;
    }
    return ans;
};
