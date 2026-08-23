// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

/**
 * @param {string} start
 * @param {string} result
 * @return {boolean}
 */
var canTransform = function(start, result) {
    let a = '', b = '';
    for (const ch of start) if (ch !== 'X') a += ch;
    for (const ch of result) if (ch !== 'X') b += ch;
    if (a !== b) return false;
    let i = 0, j = 0;
    const n = start.length;
    while (i < n && j < n) {
        while (i < n && start[i] === 'X') i++;
        while (j < n && result[j] === 'X') j++;
        if (i === n || j === n) break;
        if (start[i] !== result[j]) return false;
        if (start[i] === 'L' && i < j) return false;
        if (start[i] === 'R' && i > j) return false;
        i++;
        j++;
    }
    return true;
};
