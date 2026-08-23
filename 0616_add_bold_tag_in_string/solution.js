// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {string}
 */
var addBoldTag = function(s, words) {
    const n = s.length;
    const bold = Array(n).fill(false);
    for (const word of words) {
        let start = s.indexOf(word);
        while (start >= 0) {
            for (let i = start; i < start + word.length; ++i) bold[i] = true;
            start = s.indexOf(word, start + 1);
        }
    }
    let parts = "";
    let i = 0;
    while (i < n) {
        if (bold[i]) {
            parts += "<b>";
            while (i < n && bold[i]) parts += s[i++];
            parts += "</b>";
        } else {
            parts += s[i++];
        }
    }
    return parts;
};
