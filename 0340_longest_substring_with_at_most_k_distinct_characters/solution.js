// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
var lengthOfLongestSubstringKDistinct = function(s, k) {
    if (k === 0) return 0;

    const counts = new Map();
    let left = 0;
    let best = 0;

    for (let right = 0; right < s.length; right += 1) {
        const char = s[right];
        counts.set(char, (counts.get(char) || 0) + 1);
        while (counts.size > k) {
            const leftChar = s[left];
            counts.set(leftChar, counts.get(leftChar) - 1);
            if (counts.get(leftChar) === 0) counts.delete(leftChar);
            left += 1;
        }
        best = Math.max(best, right - left + 1);
    }

    return best;
};
