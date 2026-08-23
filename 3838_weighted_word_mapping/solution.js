// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

var mapWordWeights = function(words, weights) {
    let ans = '';
    for (const w of words) {
        let s = 0;
        for (const c of w) s = (s + weights[c.charCodeAt(0) - 97]) % 26;
        ans += String.fromCharCode(97 + (25 - s));
    }
    return ans;
};
