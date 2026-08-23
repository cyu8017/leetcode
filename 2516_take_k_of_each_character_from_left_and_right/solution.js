// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var takeCharacters = function(s, k) {
    const n = s.length;
    const cnt = [0, 0, 0];
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    if (cnt[0] < k || cnt[1] < k || cnt[2] < k) return -1;
    const need = [cnt[0] - k, cnt[1] - k, cnt[2] - k];
    const window = [0, 0, 0];
    let left = 0, maxMid = 0;
    for (let right = 0; right < n; right++) {
        window[s.charCodeAt(right) - 97]++;
        while (window[0] > need[0] || window[1] > need[1] || window[2] > need[2]) {
            window[s.charCodeAt(left) - 97]--;
            left++;
        }
        if (right - left + 1 > maxMid) maxMid = right - left + 1;
    }
    return n - maxMid;
};
