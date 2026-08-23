// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

var validSubstringCount = function(word1, word2) {
    const need = new Array(26).fill(0);
    let required = 0;
    for (const c of word2) {
        const i = c.charCodeAt(0) - 97;
        if (need[i] === 0) required++;
        need[i]++;
    }
    const have = new Array(26).fill(0);
    let formed = 0, ans = 0, l = 0;
    for (let r = 0; r < word1.length; r++) {
        const c = word1.charCodeAt(r) - 97;
        have[c]++;
        if (have[c] === need[c] && need[c] > 0) formed++;
        while (formed === required && l <= r) {
            ans += word1.length - r;
            const c2 = word1.charCodeAt(l) - 97;
            if (have[c2] === need[c2] && need[c2] > 0) formed--;
            have[c2]--;
            l++;
        }
    }
    return ans;
};
