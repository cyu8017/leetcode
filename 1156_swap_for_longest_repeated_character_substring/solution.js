// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

/**
 * @param {string} text
 * @return {number}
 */
var maxRepOpt1 = function(text) {
    const count = new Map();
    for (const ch of text) count.set(ch, (count.get(ch) || 0) + 1);
    const n = text.length;
    let ans = 0, i = 0;
    while (i < n) {
        let j = i;
        while (j < n && text[j] === text[i]) j++;
        const length = j - i;
        let k = j + 1;
        while (k < n && text[k] === text[i]) k++;
        const length2 = j < n ? k - j - 1 : 0;
        ans = Math.max(ans, Math.min(length + length2 + 1, count.get(text[i])));
        i = j;
    }
    return ans;
};
