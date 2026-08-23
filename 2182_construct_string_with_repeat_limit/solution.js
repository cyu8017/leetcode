// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

/**
 * @param {string} s
 * @param {number} repeatLimit
 * @return {string}
 */
var repeatLimitedString = function(s, repeatLimit) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) freq[s.charCodeAt(i) - 97]++;
    const ans = [];
    while (true) {
        let placed = false;
        for (let c = 25; c >= 0; c--) {
            if (freq[c] === 0) continue;
            if (ans.length > 0 && ans[ans.length - 1].charCodeAt(0) - 97 === c) {
                let found = false;
                for (let d = c - 1; d >= 0; d--) {
                    if (freq[d] > 0) {
                        ans.push(String.fromCharCode(97 + d));
                        freq[d]--;
                        found = placed = true;
                        break;
                    }
                }
                if (!found) return ans.join('');
                break;
            }
            const use = Math.min(freq[c], repeatLimit);
            for (let i = 0; i < use; i++) ans.push(String.fromCharCode(97 + c));
            freq[c] -= use;
            placed = true;
            break;
        }
        if (!placed) break;
    }
    return ans.join('');
};
