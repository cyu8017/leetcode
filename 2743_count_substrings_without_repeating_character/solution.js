// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

/**
 * @param {string} s
 * @return {number}
 */
var numberOfSpecialSubstrings = function(s) {
    const n = s.length;
    let ans = 0, left = 0;
    const cnt = Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;
        cnt[c]++;
        while (cnt[c] > 1) {
            cnt[s.charCodeAt(left) - 97]--;
            left++;
        }
        ans += i - left + 1;
    }
    return ans;
};
