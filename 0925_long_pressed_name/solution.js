// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
    let i = 0, j = 0;
    while (j < typed.length) {
        if (i < name.length && name[i] === typed[j]) { i++; j++; }
        else if (j > 0 && typed[j] === typed[j - 1]) j++;
        else return false;
    }
    return i === name.length;
};
