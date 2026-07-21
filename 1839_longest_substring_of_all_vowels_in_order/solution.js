// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

/**
 * @param {string} word
 * @return {number}
 */
var longestBeautifulSubstring = function(word) {
    const vowels = 'aeiou';
    let best = 0;
    for (let start = 0; start < word.length; start++) {
        if (word[start] !== 'a') continue;
        const counts = [0, 0, 0, 0, 0];
        for (let end = start; end < word.length; end++) {
            const current = word[end];
            if (end > start && current < word[end - 1]) break;
            const idx = vowels.indexOf(current);
            if (idx < 0) break;
            counts[idx] += 1;
            if (idx > 0 && counts[idx - 1] === 0) break;
            if (counts.every((c) => c > 0)) best = Math.max(best, end - start + 1);
        }
    }
    return best;
};
