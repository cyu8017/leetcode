// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    const b = [];
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (j < spaces.length && spaces[j] === i) { b.push(' '); j++; }
        b.push(s[i]);
    }
    return b.join('');
};
