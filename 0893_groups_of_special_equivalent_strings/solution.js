// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

/**
 * @param {string[]} words
 * @return {number}
 */
var numSpecialEquivGroups = function(words) {
    const groups = new Set();
    for (const w of words) {
        const even = [], odd = [];
        for (let i = 0; i < w.length; i++) {
            if (i % 2 === 0) even.push(w[i]);
            else odd.push(w[i]);
        }
        even.sort();
        odd.sort();
        groups.add(even.join("") + "|" + odd.join(""));
    }
    return groups.size;
};
