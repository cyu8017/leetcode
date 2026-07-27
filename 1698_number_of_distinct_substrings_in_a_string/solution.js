// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

/**
 * @param {string} s
 * @return {number}
 */
var countDistinct = function(s) {
    const root = {};
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        let node = root;
        for (let j = i; j < s.length; j++) {
            const c = s[j];
            if (!(c in node)) {
                node[c] = {};
                ans++;
            }
            node = node[c];
        }
    }
    return ans;
};
