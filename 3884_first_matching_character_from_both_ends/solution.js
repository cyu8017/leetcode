// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

var firstMatchingIndex = function(s) {
    const n = s.length;
    for (let i = 0; i < Math.floor(n / 2) + 1; i++) {
        if (s[i] === s[n - i - 1]) return i;
    }
    return -1;
};
