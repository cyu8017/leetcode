// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
    let l = 0, ans = 0;
    const cnt = new Array(26).fill(0);
    for (let r = 0; r < s.length; r++) {
        const idx = s.charCodeAt(r) - 97;
        cnt[idx]++;
        while (cnt[idx] > 2) {
            cnt[s.charCodeAt(l) - 97]--;
            l++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
};
