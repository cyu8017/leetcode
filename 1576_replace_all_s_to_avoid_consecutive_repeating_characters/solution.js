// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

/**
 * @param {string} s
 * @return {string}
 */
var modifyString = function(s) {
    const chars = s.split("");
    for (let i = 0; i < chars.length; i++) {
        if (chars[i] === "?") {
            for (const c of "abc") {
                if ((i === 0 || chars[i - 1] !== c) && (i + 1 === chars.length || chars[i + 1] !== c)) {
                    chars[i] = c;
                    break;
                }
            }
        }
    }
    return chars.join("");
};
