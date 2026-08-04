// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    const ans = [];
    for (const c of s) {
        if (ans.length >= 2 && ans[ans.length - 1] === c && ans[ans.length - 2] === c) continue;
        ans.push(c);
    }
    return ans.join("");
};
