// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const chars = s.split("");
    const n = chars.length;
    let start = 0;
    for (let i = 0; i <= n; ++i) {
        if (i === n || chars[i] === " ") {
            let left = start, right = i - 1;
            while (left < right) {
                [chars[left], chars[right]] = [chars[right], chars[left]];
                ++left;
                --right;
            }
            start = i + 1;
        }
    }
    return chars.join("");
};
