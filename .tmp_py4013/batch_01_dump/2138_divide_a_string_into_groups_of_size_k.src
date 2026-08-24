// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function(s, k, fill) {
    const ans = [];
    for (let i = 0; i < s.length; i += k) {
        if (i + k <= s.length) ans.push(s.substring(i, i + k));
        else {
            let chunk = s.substring(i);
            while (chunk.length < k) chunk += fill;
            ans.push(chunk);
        }
    }
    return ans;
};
